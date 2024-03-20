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


def ColourProfile(n):
    # to get `hsv_lower` and `hsv_upper`, `get_hsv_range()` from `tuning_utils.py` is used
    if n == 0:
        name = "nitrile glove"
        hsv_lower = (22, 0, 78)
        hsv_upper = (103, 166, 255)

    return name, hsv_lower, hsv_upper


def identifyDefectTypes_NitrileGlove(img):
    # Preprocessing the image
    blurred_img = cv2.GaussianBlur(img, (13, 13), 0)
    hsv_img = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2HSV)

    # Define the range for the color of the glove in HSV
    gloveName, hsv_lower, hsv_upper = ColourProfile(0)


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

def identifyGloveType_nitrile(img, totalGloveType_nitrile):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gloveTypeNames = []
    gloveTypeContourCounts = []
    gloveTypeContourAreas = []
    for gloveTypeIndex in range(totalGloveType_nitrile):
        gloveName, hsv_lower, hsv_higher = ColourProfile(gloveTypeIndex)
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