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

    return name, hsv_lower, hsv_upper

def identifydefectscope_nitrile():
    pass


def identify_fingertipholes_in_glove(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Start with a lower threshold that just starts to capture the holes
    thresh_level = 180  # Adjust based on the image histogram
    _, thresh = cv2.threshold(blur, thresh_level, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # You'll need to adjust these based on the actual size of the holes in pixels
    min_area = 100  # Minimum area of a hole in pixels
    max_area = 1000  # Maximum area of a hole in pixels
    holes = [cnt for cnt in contours if min_area < cv2.contourArea(cnt) < max_area]

    # Draw contours
    cv2.drawContours(img, holes, -1, (0, 255, 0), 3)
    cv2.imshow('Detected Holes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Return the number of holes detected
    return len(holes)


def identifyStain(gloveType, img):
    if gloveType != "nitrile glove":
        return "No nitrile glove detected."

    # Convert image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define HSV range for the stain color (you may need to tune this)
    stain_lower_hsv = np.array([100, 50, 50])
    stain_upper_hsv = np.array([140, 255, 255])

    # Create a mask for the stain color
    stain_mask = cv2.inRange(hsv, stain_lower_hsv, stain_upper_hsv)

    # Find contours of the stains
    contours, _ = cv2.findContours(stain_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on size or other properties
    defects = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50:  # you may need to adjust this threshold
            defects.append(cnt)

    # Return the number of defects (stains)
    num_defects = len(defects)

    # If needed, draw contours on the image for visualization
    for cnt in defects:
        cv2.drawContours(img, [cnt], 0, (0, 0, 255), 3)
    cv2.imshow('Detected Stains', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Return the count of stains detected
    return f"Detected {num_defects} fingertip stains on the nitrile glove."


# Add to algorithms.py

def identify_holes(img, hsv_lower, hsv_upper):
    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Create a mask for the color of the holes (assuming the holes will show the black background)
    # The lower and upper HSV values may need to be tuned
    mask = cv2.inRange(hsv, hsv_lower, hsv_upper)

    # Optional: Perform morphological operations to clean up the mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Find contours of the holes
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small contours that are not holes
    holes = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]  # threshold may need tuning

    # Return the mask and the contours of the holes
    return mask, holes


def identifyDefectType(gloveType, defectParams):

    pass


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
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
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

