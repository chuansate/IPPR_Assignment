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
        hsv_lower = (20, 0, 98)
        hsv_upper = (78, 130, 238)

    elif n == 2:
        name = "silicone glove"
        hsv_lower = (154, 36, 100)
        hsv_upper = (178, 116, 220)

    elif n == 3:
        name = "fabric glove"
        hsv_lower = (13, 17, 150)
        hsv_upper = (22, 88, 245)

    return name, hsv_lower, hsv_upper


def identifyDefectType(gloveType, defectParams):

    pass

def HSVRangeForDefectDetectionSiliconGlove(n):
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


def identifyGloveType(img, totalGloveType):
    # encode params of each type of glove here....
    # then scan thru to see which class suits the most....
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gloveTypeNames = []
    gloveTypeContourCounts = []
    gloveTypeContourAreas = []
    for gloveTypeIndex in range(totalGloveType):
        gloveName, hsv_lower, hsv_higher = colourProfiles(gloveTypeIndex)
        gloveTypeNames.append(gloveName)
        # create a binary mask where:
        # wanted parts are in white
        # unwanted parts are in black
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
        cv2.imshow(gloveName, imgCopy)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("gloveTypeContourCounts = ", gloveTypeContourCounts)
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



def detectGloveDefects(img):
    # Convert image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mould_defect = False
    mark_defect = False
    missing_fingers = False
    for i in range(1,3):
        name, hue_lower, hue_upper, saturation_lower, saturation_upper, value_lower, value_upper, threshold_value, min_contour_area, blur_value = HSVRangeForDefectDetectionSiliconGlove(i)

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

        # cv2.imshow("Result Image", img_copy)
        # cv2.waitKey(0)
        # print(contours)
        # print("lower :", lower)
        # print("upper :", upper)
        # print("threshold:", threshold_value)
        # print("area:", min_contour_area)
        # print("Blur: ", blur_value)

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


def detectGloveDefectType(img):
    mould_defect, mark_defect, missing_fingers, img_copy = detectGloveDefects(img)
    if mould_defect:
        print("The defect identified is mould found in glove")
        cv2.putText(img_copy, "Defect = Mould found on glove", (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
        # Display the result
        cv2.imshow("mould Defect", img_copy)
        cv2.waitKey(0)
    elif mark_defect:
        print("The defect identified is mark found in glove")
        cv2.putText(img_copy, "Defect = Mark found on glove", (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
        # Display the result
        cv2.imshow("mark Defect", img_copy)
        cv2.waitKey(0)
    else:
        print("The defect identified is missing fingers in glove")
        cv2.putText(img_copy, "Defect = Missing fingers in glove", (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
        # Display the result
        cv2.imshow("missing Finger Defect", img_copy)
        cv2.waitKey(0)