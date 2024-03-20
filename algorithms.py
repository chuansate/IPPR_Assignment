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

