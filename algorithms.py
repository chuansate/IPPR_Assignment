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


def identifyDefectType_MedicalGlove(img):
    # to remove the wrinkles on the gloves with holes and missing finger
    img = cv2.GaussianBlur(img, (21, 21), 0)
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
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    glove_contour = contours[0]
    glove_mask = np.zeros_like(gray)

    # drawing the glove contour, thickness=-1 means filling the glove
    # cv2.drawContours(glove_mask, [glove_contour], -1, 255, thickness=-1)

    # Filter contours based on area (you can adjust the threshold)
    # for contour in contours:
    #     area = cv2.contourArea(contour)
    #     if area < 1000:  # Adjust this threshold as needed
    #         hole_contours.append(contour)

    # do the filtering on second-largest blob based on circularity, area, maybe aspect ratio?
    # the threshold is again gotten thru trackbars, then encode them!
    print("len of contours = ", len(contours))

    # refer https://docs.opencv.org/4.x/d9/d8b/tutorial_py_contours_hierarchy.html
    print("hierarchy = ", hierarchy)
    if len(contours) >= 2:
        # dirty and stain analysis + hole analysis
        hole_contour = contours[2]  # filter the blobs based on areas to see which one is hole
        cv2.drawContours(img, [hole_contour], -1, (0, 255, 0), 3)
        cv2.imshow("Glove with hole", img)
        cv2.waitKey(0)
    elif len(contours) == 1:
        # missing finger analysis
        print("Missing finger!")
    else:
        # no contour, means don't belong to any defect type
        print("Unknown defect type!")


    # cv2.imshow("Wanted parts", wantedParts)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Glove mask", glove_mask)
    cv2.waitKey(0)


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

