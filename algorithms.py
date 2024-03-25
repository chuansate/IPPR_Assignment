"""
Algorithms to process the images
"""
import cv2
import numpy as np

def colourProfiles(n):
    # to get `hsv_lower` and `hsv_upper`, `get_hsv_range()` from `tuning_utils.py` is used
    if n == 0:
        name = "medical glove"
        hsv_lower = (99, 152, 41)
        hsv_upper = (114, 255, 235)

    elif n == 1:
        name = "nitrile glove"
        # hsv_lower = (20, 0, 98)
        # hsv_upper = (78, 130, 238)
        hsv_lower = (20, 0, 98)
        hsv_upper = (78, 130, 255)

    elif n == 2:
        name = "silicone glove"
        hsv_lower = (154, 36, 100)
        hsv_upper = (178, 116, 220)

    elif n == 3:
        name = "fabric glove"
        hsv_lower = (13, 17, 150)
        hsv_upper = (22, 88, 245)

    return name, hsv_lower, hsv_upper

def identifyGloveType(img, totalGloveType):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gloveTypeNames = []
    gloveTypeContourCounts = []
    gloveTypeContourAreas = []
    for gloveTypeIndex in range(totalGloveType):
        gloveName, hsv_lower, hsv_higher = colourProfiles(gloveTypeIndex)
        gloveTypeNames.append(gloveName)
        # create a binary mask where: wanted parts are in white, unwanted parts are in black
        mask = cv2.inRange(hsv, hsv_lower, hsv_higher)
        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # -1 signifies drawing all contours
        gloveTypeContourCounts.append(len(contours))
        if len(contours) != 0:
            cnt = contours[0]
            gloveTypeContourAreas.append(cv2.contourArea(cnt))
        else:
            gloveTypeContourAreas.append(0)
        imgCopy = img.copy()
        cv2.drawContours(imgCopy, contours, -1, (0, 255, 0), 3)

    countOf1 = 0
    indexesOf1_gloveTypeContourCounts = []
    # if there is a 1 only in gloveTypeContourCounts, return the index!
    for i, count in enumerate(gloveTypeContourCounts):
        if count == 1:
            countOf1 = countOf1 + 1
            indexesOf1_gloveTypeContourCounts.append(i)
    # if there are multiple 1 in gloveTypeContourCounts, compare the areas and return the index with largest areas!
    if countOf1 > 1:
        # compute the areas and return the index with largest areas
        contourAreas = []
        for index in indexesOf1_gloveTypeContourCounts:
            contourAreas.append(gloveTypeContourAreas[index])
        return gloveTypeNames[contourAreas.index(max(contourAreas))]
    elif countOf1 == 1:
        return gloveTypeNames[indexesOf1_gloveTypeContourCounts[0]]
    else: # there is no 1 in `gloveTypeContourCounts`
    # else return the index with least gloveTypeContourCounts but greater than 0
        for i, count in enumerate(gloveTypeContourCounts):
            if count == 0:
                gloveTypeContourCounts[i] = max(gloveTypeContourCounts) + 1
        return gloveTypeNames[gloveTypeContourCounts.index(min(gloveTypeContourCounts))]

def calculateShapeFactor_FabricGlove(contour):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    shape_factor = (perimeter ** 2) / (4 * np.pi * area)
    return shape_factor

def identifyDefectType_FabricGlove(image, thresh, minDefect, maxDefect):
    # preprocessing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # number of defect detection
    filtered_contours = [cnt for cnt in contours if minDefect < cv2.contourArea(cnt) < maxDefect]
    num_defects = len(filtered_contours)
    shape_factor = 0
    print('Number of defects:', num_defects)
    for defect in filtered_contours:
        shape_factor = calculateShapeFactor_FabricGlove(defect)
        print('Shape factor:', shape_factor)
        cv2.drawContours(image, [defect], -1, (0,255,0), 3)

    # defect identification
    if shape_factor > 6 and num_defects == 1:
       defect_type = 'Opening Defect'
    elif shape_factor > 1 and num_defects > 1:
        defect_type = 'Multiple Stains Defect'
    elif shape_factor == 0 and num_defects == 0:
        defect_type = 'Stitch Defect'
    
    # Display results
    cv2.putText(image, 'Glove Type = Fabric Glove', (5, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 234, 255), 2, cv2.LINE_AA)
    cv2.putText(image, f'Defect Type = {defect_type}', (5, 80), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 234, 255), 2, cv2.LINE_AA)
    cv2.imshow(f'{defect_type} detected', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def identifyDefectType_MedicalGlove(img, minDirtyArea, maxDirtyArea, minPartialTearArea, maxPartialTearArea, minDirtyEcc, maxDirtyEcc, minPartialTearEcc, maxPartialTearEcc):
    # to remove the wrinkles on the gloves with holes and missing finger
    img = cv2.GaussianBlur(img, (15, 15), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gloveName, hsv_lower, hsv_higher = colourProfiles(0)
    # create a binary mask where: wanted parts are in white, unwanted parts are in black
    mask = cv2.inRange(hsv, hsv_lower, hsv_higher)
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    edges = cv2.Canny(mask, 30, 100)
    # Assuming the glove is the largest connected component
    # the defect is juz the second-largest blobs
    # `cv2.RETR_TREE` retrieves all the contours and creates a full family hierarchy list
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    glove_contour = contours[0]
    glove_mask = np.zeros_like(gray)
    if len(contours) >= 2:
        dirty_contour = None
        partialTear_contour = None
        for i in range(1, len(contours)):
            cnt = contours[i]
            cntArea = cv2.contourArea(cnt)
            eccentricity = 0
            if len(cnt) >= 5: # FitEllipse requires at least 5 points
                ellipse = cv2.fitEllipse(cnt)
                # Extract the lengths of the major and minor axes
                major_axis = max(ellipse[1])
                minor_axis = min(ellipse[1])
                # Calculate the eccentricity of the ellipse
                eccentricity = (major_axis - minor_axis) / major_axis

            if minDirtyArea <= cntArea <= maxDirtyArea and minDirtyEcc <= eccentricity <= maxDirtyEcc:
                dirty_contour = cnt
                break
            elif minPartialTearArea <= cntArea <= maxPartialTearArea and minPartialTearEcc <= eccentricity <= maxPartialTearEcc:
                partialTear_contour = cnt
                break
        if dirty_contour is not None:
            cv2.putText(img, 'Glove Type = Medical Glove', (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(img, 'Defect Type = Dirty', (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.drawContours(img, [dirty_contour], -1, (0, 255, 0), 3)
            cv2.imshow("Img with dirty detected", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        if partialTear_contour is not None:
            cv2.putText(img, 'Glove Type = Medical Glove', (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(img, 'Defect Type = Partial Tear', (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.drawContours(img, [partialTear_contour], -1, (0, 255, 0), 3)
            cv2.imshow("Img with partial tear detected", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        if dirty_contour is None and partialTear_contour is None:
            # then we can determine based on the difference of area betw first largest and second largest
            # or maybe based on aspect ratio, circularity, other geometric measures
            cv2.putText(img, 'Glove Type = Medical Glove', (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(img, 'Defect Type = Fingertip tear', (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
            cv2.imshow("Img with fingertip tear detected", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            return "Fingertip tear"

    elif len(contours) == 1:
        cv2.putText(img, 'Glove Type = Medical Glove', (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(img, 'Defect Type = Fingertip tear', (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.drawContours(img, [contours], -1, (0, 255, 0), 3)
        cv2.imshow("Img with fingertip tear detected", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return "Fingertip tear"

    else:
        return "Unknown defect type"

def ColourProfile_NitrileGlove(n):
    # to get `hsv_lower` and `hsv_upper`, `get_hsv_range()` from `tuning_utils.py` is used
    if n == 0:
        name = "nitrile glove"
        hsv_lower = (22, 0, 78)
        hsv_upper = (103, 166, 255)

    return name, hsv_lower, hsv_upper

def identifyGloveType_Nitrile(img, totalGloveType_nitrile):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gloveTypeNames = []
    gloveTypeContourCounts = []
    gloveTypeContourAreas = []
    for gloveTypeIndex in range(totalGloveType_nitrile):
        gloveName, hsv_lower, hsv_higher = ColourProfile_NitrileGlove(gloveTypeIndex)
        gloveTypeNames.append(gloveName)
        # create a binary mask where: wanted parts are in white, unwanted parts are in black
        mask = cv2.inRange(hsv, hsv_lower, hsv_higher)
        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # -1 signifies drawing all contours
        gloveTypeContourCounts.append(len(contours))
        if len(contours) != 0:
            cnt = contours[0]
            gloveTypeContourAreas.append(cv2.contourArea(cnt))
        else:
            gloveTypeContourAreas.append(0)
        imgCopy = img.copy()
        cv2.drawContours(imgCopy, contours, -1, (0, 255, 0), 3)

    countOf1 = 0
    indexesOf1_gloveTypeContourCounts = []
    # if there is a 1 only in gloveTypeContourCounts, return the index!
    for i, count in enumerate(gloveTypeContourCounts):
        if count == 1:
            countOf1 = countOf1 + 1
            indexesOf1_gloveTypeContourCounts.append(i)
    # if there are multiple 1 in gloveTypeContourCounts, compare the areas and return the index with largest areas!
    if countOf1 > 1:
        # compute the areas and return the index with largest areas
        contourAreas = []
        for index in indexesOf1_gloveTypeContourCounts:
            contourAreas.append(gloveTypeContourAreas[index])
        return gloveTypeNames[contourAreas.index(max(contourAreas))]
    elif countOf1 == 1:
        return gloveTypeNames[indexesOf1_gloveTypeContourCounts[0]]
    else: # there is no 1 in `gloveTypeContourCounts`
    # else return the index with least gloveTypeContourCounts but greater than 0
        for i, count in enumerate(gloveTypeContourCounts):
            if count == 0:
                gloveTypeContourCounts[i] = max(gloveTypeContourCounts) + 1
        return gloveTypeNames[gloveTypeContourCounts.index(min(gloveTypeContourCounts))]

def identifyDefectTypes_NitrileGlove(img):
    # Preprocessing the image
    blurred_img = cv2.GaussianBlur(img, (13, 13), 0)
    hsv_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2HSV)

    # Define the range for the color of the glove in HSV
    gloveName, hsv_lower, hsv_upper = ColourProfile_NitrileGlove(0)

    # Define the range for the color of the stains in HSV
    lower_hsv_stain = np.array([63, 85, 81])
    upper_hsv_stain = np.array([128, 255, 255])

    # Create binary masks
    mask_glove = cv2.inRange(hsv_img, hsv_lower, hsv_upper)
    mask_stains = cv2.inRange(hsv_img, lower_hsv_stain, upper_hsv_stain)

    # Combine the masks if necessary, or keep separate if using different criteria for defects
    combined_mask = cv2.bitwise_or(mask_glove, mask_stains)

    kernel = np.ones((3, 3), np.uint8)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel, iterations=2)

    # Find contours on the combined mask
    contours, hierarchy = cv2.findContours(combined_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through the contours to find holes and stains
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if hierarchy[0, i, 3] != -1:    # Child contour (potential hole)
            mix_contour_found = False
            if 100 <= area <= 300 and 300 <= area <= 450:
                cv2.drawContours(img, [contour], -1, (0, 0, 255), 3)  # Using blue for mixed defects
                cv2.putText(img, 'Mixed Defect Detected', (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.imshow('Detected Mixed Defects', img)

        # Parent contour (potential stain)
            elif 300 <= area <= 450:  # Adjust area range for stain as needed
                # Draw the contour that is identified as a stain
                cv2.drawContours(img, [contour], -1, (255, 0, 0), 3)
                cv2.imshow('Detected Stain Defects', img)

            elif 100 <= area <= 300:  # Adjust area range for holes as needed
                # Draw the contour that is identified as a hole
                cv2.drawContours(img, [contour], -1, (0, 255, 0), 3)
                cv2.imshow('Detected Hole Defects', img)

            elif 200 <= area <= 700:  # Adjust area range for fingertip holes as needed
                # Draw the contour that is identified as a fingertip hole
                cv2.drawContours(img, [contour], -1, (0, 255, 0), 3)
                cv2.imshow('Detected FingerTip Hole Defects', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def HSVRangeForDefectDetection_SiliconeGlove(n):
    if n == 1:
        name = "mark detection"
        hue_lower = 0
        hue_upper = 180
        saturation_lower = 0
        saturation_upper = 30
        value_lower = 0
        value_upper = 30
        threshold = 0
        min_contour_area = 100
        blur_value = (5) * 2+1

    elif n == 2:
        name = "mould detection"
        hue_lower = 18
        hue_upper = 63
        saturation_lower = 50
        saturation_upper = 80
        value_lower = 95
        value_upper = 148
        threshold = 0
        min_contour_area = 500
        blur_value = (4) * 2+1

    return name, hue_lower, hue_upper, saturation_lower, saturation_upper, value_lower, value_upper, threshold, min_contour_area, blur_value

def detectGloveDefects_SiliconeGlove(img):
    # Convert image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mould_defect = False
    mark_defect = False
    missing_fingers = False
    for i in range(1,3):
        name, hue_lower, hue_upper, saturation_lower, saturation_upper, value_lower, value_upper, threshold_value, min_contour_area, blur_value = HSVRangeForDefectDetection_SiliconeGlove(i)

        lower = np.array([hue_lower, saturation_lower, value_lower])
        upper = np.array([hue_upper, saturation_upper, value_upper])

        # Create a mask for the selected color range
        mask = cv2.inRange(hsv, lower, upper)

        # Apply Gaussian blur
        mask = cv2.GaussianBlur(mask, (blur_value, blur_value), 0)

        # Apply thresholding to create a binary mask
        _, mask = cv2.threshold(mask, threshold_value, 255, cv2.THRESH_BINARY)

        # Apply morphological operations to remove noise
        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Create a copy of the original image
        img_copy = img.copy()

        # Filter contours by minimum area
        contours = [contour for contour in contours if cv2.contourArea(contour) > min_contour_area]

        cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2)

        if len(contours) == 1 and i == 2:
            # Draw contours for pink glove, black marks, and green mold
            cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2)
            mould_defect = True
            break

        if len(contours) == 1 and i == 1:
            # Draw contours for pink glove, black marks, and green mold
            cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2)
            mark_defect = True
            break


    return mould_defect, mark_defect, missing_fingers, img_copy

def identifyDefectType_SiliconeGlove(img):
    mould_defect, mark_defect, missing_fingers, img_copy = detectGloveDefects_SiliconeGlove(img)
    if mould_defect:
        print("The defect identified is mould found in glove")
        cv2.putText(img_copy, "Defect = Mould found on glove", (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
        # Display the result
        cv2.imshow("mould Defect", img_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif mark_defect:
        print("The defect identified is mark found in glove")
        cv2.putText(img_copy, "Defect = Mark found on glove", (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
        # Display the result
        cv2.imshow("mark Defect", img_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("The defect identified is missing fingers in glove")
        cv2.putText(img_copy, "Defect = Missing fingers in glove", (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
        # Display the result
        cv2.imshow("missing Finger Defect", img_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
