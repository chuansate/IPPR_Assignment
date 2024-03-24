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

def calculate_shape_factor(contour):
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
        shape_factor = calculate_shape_factor(defect)
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