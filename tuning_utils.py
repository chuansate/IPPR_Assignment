"""
- functions to tune the params for identifying the type of glove based on HSV color space
- functions to tune the params for identifying the type of defect based on the geometric properties
"""

import cv2
import numpy as np

medicalGlove1 = cv2.imread("Glove_images/medical/dirty/dirty1.jpeg")
medicalGlove2 = cv2.imread("Glove_images/medical/dirty/dirty2.jpeg")
nitrileGlove1 = cv2.imread("Glove_images/nitrile/fingertip_hole/NITRILE FINGER HOLE 1.jpg")
nitrileGlove2 = cv2.imread("Glove_images/nitrile/fingertip_hole/NITRILE FINGER HOLE 2.jpg")
nitrileGlove3 = cv2.imread("Glove_images/nitrile/fingertip_stain/NITRILE FINGER STAIN 1.jpg")
nitrileGlove4 = cv2.imread("Glove_images/nitrile/fingertip_stain/NITRILE FINGER STAIN 2.jpg")
nitrileGlove5 = cv2.imread("Glove_images/nitrile/hole/NITRILE HOLE 1.jpg")
nitrileGlove6 = cv2.imread("Glove_images/nitrile/hole/NITRILE HOLE 2.jpg")
nitrileGlove7 = cv2.imread("Glove_images/nitrile/stain/NITRILE STAIN 1.jpg")
nitrileGlove8 = cv2.imread("Glove_images/nitrile/stain/NITRILE STAIN 2.jpg")
nitrileGlove9 = cv2.imread("Glove_images/nitrile/mix/NITRILE MIX 1.jpg")
nitrileGlove10 = cv2.imread("Glove_images/nitrile/mix/NITRILE MIX 2.jpg")
siliconeGlove1 = cv2.imread("Glove_images/silicone/mould/mould_1.jpeg")
siliconeGlove2 = cv2.imread("Glove_images/silicone/mould/mould_2.jpeg")
siliconeGlove3 = cv2.imread("Glove_images/silicone/mould/mould_3.jpeg")
fabricGlove1 = cv2.imread("Glove_images/fabric/multiple_stains/multiple_stains1.jpg")
fabricGlove2 = cv2.imread("Glove_images/fabric/multiple_stains/multiple_stains2.jpg")

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


# get_hsv_range_with_morphological_operations(nitrileGlove5)
# get_hsv_range_with_morphological_operations(nitrileGlove6)

def onTrackbarChange(value):
    pass

def detectGloveTrackbar(img):
    cv2.namedWindow("Trackbars", cv2.WINDOW_NORMAL)  # Set window to allow resizing

    # Adjust the size of the trackbar window to match the image size
    trackbar_width = 400
    trackbar_height = img.shape[0] + 50  # Add extra height for trackbar labels
    cv2.resizeWindow("Trackbars", trackbar_width, trackbar_height)

    # Create trackbars for adjusting HSV color ranges
    cv2.createTrackbar("Hue Lower", "Trackbars", 0, 180, onTrackbarChange)
    cv2.createTrackbar("Hue Upper", "Trackbars", 180, 180, onTrackbarChange)
    cv2.createTrackbar("Saturation Lower", "Trackbars", 0, 255, onTrackbarChange)
    cv2.createTrackbar("Saturation Upper", "Trackbars", 255, 255, onTrackbarChange)
    cv2.createTrackbar("Value Lower", "Trackbars", 0, 255, onTrackbarChange)
    cv2.createTrackbar("Value Upper", "Trackbars", 255, 255, onTrackbarChange)
    cv2.createTrackbar("Threshold", "Trackbars", 127, 255, onTrackbarChange)
    cv2.createTrackbar("Min Contour Area", "Trackbars", 100, 5000, onTrackbarChange)
    cv2.createTrackbar("Gaussian Blur", "Trackbars", 0, 10, onTrackbarChange)

    while True:
        # Get current trackbar positions
        hue_lower = cv2.getTrackbarPos("Hue Lower", "Trackbars")
        hue_upper = cv2.getTrackbarPos("Hue Upper", "Trackbars")
        saturation_lower = cv2.getTrackbarPos("Saturation Lower", "Trackbars")
        saturation_upper = cv2.getTrackbarPos("Saturation Upper", "Trackbars")
        value_lower = cv2.getTrackbarPos("Value Lower", "Trackbars")
        value_upper = cv2.getTrackbarPos("Value Upper", "Trackbars")
        threshold_value = cv2.getTrackbarPos("Threshold", "Trackbars")
        min_contour_area = cv2.getTrackbarPos("Min Contour Area", "Trackbars")
        blur_value = cv2.getTrackbarPos("Gaussian Blur", "Trackbars") * 2 + 1

        # Convert image to HSV color space
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Define color range based on trackbar positions
        lower = np.array([hue_lower, saturation_lower, value_lower])
        upper = np.array([hue_upper, saturation_upper, value_upper])

        print("lower :", lower)
        print("upper :", upper)
        print("threshold:", threshold_value)
        print("area:", min_contour_area)
        print("Blur: ", blur_value)
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

        # Draw contours
        cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2)

        cv2.putText(img_copy, "Number of contor :" + str(len(contours)), (30, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
        # Display the result
        cv2.imshow("Glove Defects", img_copy)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Destroy all windows
    cv2.destroyAllWindows()