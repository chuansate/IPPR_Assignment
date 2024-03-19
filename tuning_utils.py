"""
- functions to tune the params for identifying the type of glove based on HSV color space
- functions to tune the params for identifying the type of defect based on the geometric properties
"""

import cv2
import numpy as np

medicalGlove1 = cv2.imread("Glove_images/medical/dirty_and_stain/dirty_and_stain_1.jpeg")
medicalGlove2 = cv2.imread("Glove_images/medical/dirty_and_stain/dirty_and_stain_2.jpeg")
nitrileGlove1 = cv2.imread("Glove_images/nitrile/STAIN/NITRILE STAIN 1.jpg")
nitrileGlove2 = cv2.imread("Glove_images/nitrile/STAIN/NITRILE STAIN 1.jpg")
siliconeGlove1 = cv2.imread("Glove_images/silicone/mould/mould_1.jpeg")
siliconeGlove2 = cv2.imread("Glove_images/silicone/mould/mould_2.jpeg")


def empty(a):
    pass


# To adjust the track bar until the binary mask shows all the wanted parts in white, otherwise in black.
# Then, record the HSV lower and upper range, and encode them into `algorithms.py`
def get_hsv_range(img):
    cv2.namedWindow("TrackBars Window")
    cv2.resizeWindow("TrackBars Window", 640, 240)
    cv2.createTrackbar("Hue Min", "TrackBars Window", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "TrackBars Window", 179, 179, empty)
    cv2.createTrackbar("Saturation Min", "TrackBars Window", 0, 255, empty)
    cv2.createTrackbar("Saturation Max", "TrackBars Window", 255, 255, empty)
    cv2.createTrackbar("Value Min", "TrackBars Window", 0, 255, empty)
    cv2.createTrackbar("Value Max", "TrackBars Window", 255, 255, empty)
    while True:
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # "getTrackbarPos" is to get the current trackbar value
        h_min = cv2.getTrackbarPos("Hue Min", "TrackBars Window")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBars Window")
        s_min = cv2.getTrackbarPos("Saturation Min", "TrackBars Window")
        s_max = cv2.getTrackbarPos("Saturation Max", "TrackBars Window")
        v_min = cv2.getTrackbarPos("Value Min", "TrackBars Window")
        v_max = cv2.getTrackbarPos("Value Max", "TrackBars Window")
        # Create a "mask" to filter out the unwanted parts.
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        # "imgHSV" is an input image (equivalent to a 3D array).
        # `inRange()` is to create a mask for an image, where the wanted parts are in white while the unwanted parts are in black
        mask = cv2.inRange(imgHSV, lower, upper)

        # "bitwise_and" is to display the wanted part in its original color while the unwanted part will be displayed in black
        wantedParts = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow("Original Image", img)
        cv2.imshow("HSV Image", imgHSV)
        cv2.imshow("Mask Window", mask)
        cv2.imshow("Wanted parts", wantedParts)
        if cv2.waitKey(500) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


# To adjust the track bar until the binary mask shows all the wanted parts in white, otherwise in black.
# Then, record the HSV lower and upper range, and encode them into `algorithms.py`
def get_hsv_range_with_morphological_operations(img):
    cv2.namedWindow("TrackBars Window")
    cv2.resizeWindow("TrackBars Window", 640, 240)
    cv2.createTrackbar("Hue Min", "TrackBars Window", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "TrackBars Window", 179, 179, empty)
    cv2.createTrackbar("Saturation Min", "TrackBars Window", 0, 255, empty)
    cv2.createTrackbar("Saturation Max", "TrackBars Window", 255, 255, empty)
    cv2.createTrackbar("Value Min", "TrackBars Window", 0, 255, empty)
    cv2.createTrackbar("Value Max", "TrackBars Window", 255, 255, empty)
    while True:
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # "getTrackbarPos" is to get the current trackbar value
        h_min = cv2.getTrackbarPos("Hue Min", "TrackBars Window")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBars Window")
        s_min = cv2.getTrackbarPos("Saturation Min", "TrackBars Window")
        s_max = cv2.getTrackbarPos("Saturation Max", "TrackBars Window")
        v_min = cv2.getTrackbarPos("Value Min", "TrackBars Window")
        v_max = cv2.getTrackbarPos("Value Max", "TrackBars Window")
        # Create a "mask" to filter out the unwanted parts.
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        # "imgHSV" is an input image (equivalent to a 3D array).
        # `inRange()` is to create a mask for an image, where the wanted parts are in white while the unwanted parts are in black
        mask = cv2.inRange(imgHSV, lower, upper)
        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
        imgContours = img.copy()
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 3)
        cv2.putText(imgContours, "num of contours = " + str(len(contours)), (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        # "bitwise_and" is to display the wanted part in its original color while the unwanted part will be displayed in black
        wantedParts = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow("Original Image", img)
        cv2.imshow("Image with contours", imgContours)
        cv2.imshow("Mask Window", mask)
        cv2.imshow("Wanted parts", wantedParts)
        if cv2.waitKey(500) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


# get_hsv_range_with_morphological_operations(medicalGlove1)

# get_hsv_range(siliconeGlove1)
# get_hsv_range(siliconeGlove2)
# get_hsv_range(nitrileGlove1) # Assuming 'nitrileGlove1' is a variable holding the image of a nitrile glove
# get_hsv_range(nitrileGlove2)
# get_hsv_range(medicalGlove1)
# get_hsv_range(medicalGlove2)



