"""
Tune the params for segmenting a glove from an image
"""
import cv2
import numpy as np


img1 = cv2.imread('./Glove_defect_detection.v1i.multiclass/train/IMG20220420170224_jpg.rf.547b0628d51c7a5e14f9e9f5ae763913.jpg')
img2 = cv2.imread("./Glove_defect_detection.v1i.multiclass/train/IMG20220420170234_jpg.rf.6004d016cef1a1547296bd26d0dd9398.jpg")


def nothing(x):
    return x


def segment_glove_canny_trackbars(image):
    cv2.namedWindow("Trackbars")
    cv2.createTrackbar('kernel_size', 'Trackbars', 1, 21, nothing)
    cv2.createTrackbar('t_lower', 'Trackbars', 0, 255, nothing)
    cv2.createTrackbar('t_upper', 'Trackbars', 0, 255, nothing)
    cv2.setTrackbarPos("t_upper", "Trackbars", 255)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.equalizeHist(gray_image)

    while True:
        kernel_size = cv2.getTrackbarPos('kernel_size', 'Trackbars')
        kernel_erosion_dilation = np.ones((5, 5), np.uint8)
        t_lower = cv2.getTrackbarPos('t_lower', 'Trackbars')
        t_upper = cv2.getTrackbarPos('t_upper', 'Trackbars')
        if kernel_size % 2 == 0:
            kernel_size += 1
            cv2.setTrackbarPos("kernel_size", "Trackbars", kernel_size)
        blurred_image = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)
        # Apply Canny edge detector
        edges = cv2.Canny(blurred_image, t_lower, t_upper)
        edges_opened = cv2.morphologyEx(edges, cv2.MORPH_OPEN, kernel_erosion_dilation)
        # edges = cv2.dilate(edges, kernel_erosion_dilation, iterations=1)
        # Find contours in the edge-detected image
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        h, w = edges.shape[:2]
        glove_mask = np.zeros((h + 2, w + 2), np.uint8)
        im_floodfill = edges.copy()
        cv2.floodFill(im_floodfill, glove_mask, (0, 0), 255)
        cv2.drawContours(glove_mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
        # Bitwise AND to obtain the segmented glove region
        # segmented_glove = cv2.bitwise_and(image, image, mask=glove_mask)
        # Display the results
        cv2.imshow('Original Image', image)
        cv2.imshow("Edges", edges)
        cv2.imshow("Opened Edges", edges_opened)
        cv2.imshow('Floodfilled image', im_floodfill)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


# suitable for segmenting medical gloves becoz each medical glove is of one colour
def segment_glove_thresholding_trackbars(rgb_image):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 500, 500)
    cv2.createTrackbar('kernel_blur', 'Trackbars', 1, 21, nothing)
    cv2.createTrackbar('kernel_opening', 'Trackbars', 0, 255, nothing)
    cv2.createTrackbar('lower_thres', 'Trackbars', 0, 255, nothing)
    cv2.createTrackbar('upper_thres', 'Trackbars', 0, 255, nothing)
    cv2.createTrackbar('contrast', 'Trackbars', 1, 10, nothing)
    cv2.createTrackbar('brightness', 'Trackbars', 0, 127, nothing)
    cv2.setTrackbarMin('brightness', 'Trackbars', -127)
    cv2.setTrackbarPos("upper_thres", "Trackbars", 255)
    while True:
        brightness = cv2.getTrackbarPos('brightness', 'Trackbars')
        contrast = cv2.getTrackbarPos('contrast', 'Trackbars')
        rgb_image_converted = cv2.convertScaleAbs(rgb_image, alpha=contrast, beta=brightness)
        gray_image = cv2.cvtColor(rgb_image_converted, cv2.COLOR_BGR2GRAY)
        kernel_blur = cv2.getTrackbarPos('kernel_blur', 'Trackbars')
        kernel_opening_size = cv2.getTrackbarPos('kernel_opening', 'Trackbars')
        kernel_opening = np.ones((kernel_opening_size, kernel_opening_size), np.uint8)
        lower_thres = cv2.getTrackbarPos('lower_thres', 'Trackbars')
        upper_thres = cv2.getTrackbarPos('upper_thres', 'Trackbars')
        if kernel_blur % 2 == 0:
            kernel_blur += 1
            cv2.setTrackbarPos("kernel_blur", "Trackbars", kernel_blur)
        blurred_image = cv2.GaussianBlur(gray_image, (kernel_blur, kernel_blur), 0)
        th, binary_img = cv2.threshold(blurred_image, lower_thres, upper_thres, cv2.THRESH_BINARY_INV)
        binary_opened = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel_opening)
        output_img = cv2.bitwise_and(rgb_image, rgb_image, mask=binary_opened)

        # Display the results
        cv2.imshow('Original Image', rgb_image)
        cv2.imshow('Image after contrast and brightness', rgb_image_converted)
        cv2.imshow("Binary image", binary_img)
        cv2.imshow("Opened binary image", binary_opened)
        cv2.imshow('Segmented glove', output_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


def segment_glove_adaptive_thresholding_trackbars(rgb_image):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 500, 500)
    cv2.createTrackbar('kernel_blur', 'Trackbars', 1, 21, nothing)
    cv2.createTrackbar('kernel_opening', 'Trackbars', 0, 255, nothing)
    cv2.createTrackbar('blockSize', 'Trackbars', 3, 31, nothing)
    cv2.createTrackbar('C', 'Trackbars', 0, 255, nothing)
    cv2.createTrackbar('adaptiveMethod', 'Trackbars', 0, 1, nothing)
    cv2.createTrackbar('brightness', 'Trackbars', 0, 127, nothing)
    cv2.setTrackbarMin('brightness', 'Trackbars', -127)
    cv2.createTrackbar('contrast', 'Trackbars', 1, 255, nothing)
    adaptiveMethods = [cv2.ADAPTIVE_THRESH_MEAN_C, cv2.ADAPTIVE_THRESH_GAUSSIAN_C]
    while True:
        brightness = cv2.getTrackbarPos('brightness', 'Trackbars')
        contrast = cv2.getTrackbarPos('contrast', 'Trackbars')
        blockSize = cv2.getTrackbarPos('blockSize', 'Trackbars')
        adaptiveMethod_index = cv2.getTrackbarPos('adaptiveMethod', 'Trackbars')
        C = cv2.getTrackbarPos('C', 'Trackbars')
        rgb_image_converted = cv2.convertScaleAbs(rgb_image, alpha=contrast, beta=brightness)
        gray_image = cv2.cvtColor(rgb_image_converted, cv2.COLOR_BGR2GRAY)
        kernel_blur = cv2.getTrackbarPos('kernel_blur', 'Trackbars')
        kernel_opening_size = cv2.getTrackbarPos('kernel_opening', 'Trackbars')
        kernel_opening = np.ones((kernel_opening_size, kernel_opening_size), np.uint8)

        if kernel_blur % 2 == 0:
            kernel_blur += 1
            cv2.setTrackbarPos("kernel_blur", "Trackbars", kernel_blur)

        if blockSize % 2 == 0:
            blockSize += 1
            cv2.setTrackbarPos("blockSize", "Trackbars", blockSize)

        blurred_image = cv2.GaussianBlur(gray_image, (kernel_blur, kernel_blur), 0)
        binary_img = cv2.adaptiveThreshold(blurred_image, 255, adaptiveMethods[adaptiveMethod_index], cv2.THRESH_BINARY, blockSize, C)
        binary_opened = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel_opening)
        output_img = cv2.bitwise_and(rgb_image, rgb_image, mask=binary_opened)

        # Display the results
        cv2.imshow('Original Image', rgb_image)
        cv2.imshow('Image after contrast and brightness', rgb_image_converted)
        cv2.imshow("Binary image", binary_img)
        cv2.imshow("Opened binary image", binary_opened)
        cv2.imshow('Segmented glove', output_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


segment_glove_thresholding_trackbars(img1)
segment_glove_adaptive_thresholding_trackbars(img1)
