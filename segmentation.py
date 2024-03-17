"""
For segmenting a glove from an image, current file contains several methods
"""
import numpy as np
import cv2
img1 = cv2.imread('./Glove_defect_detection.v1i.multiclass/train/IMG20220420170224_jpg.rf.547b0628d51c7a5e14f9e9f5ae763913.jpg')
img2 = cv2.imread("./Glove_defect_detection.v1i.multiclass/train/IMG20220420170234_jpg.rf.6004d016cef1a1547296bd26d0dd9398.jpg")


def nothing(x):
    return x


def segment_glove_canny(image, kernel_size, t_lower, t_upper):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.equalizeHist(gray_image)
    # Apply Gaussian blur to reduce noise and improve edge detection
    blurred_image = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)
    # Apply Canny edge detector
    edges = cv2.Canny(blurred_image, t_lower, t_upper)
    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a binary mask for the glove region
    h, w = edges.shape[:2]
    glove_mask = np.zeros((h+2, w+2), np.uint8)
    im_floodfill = edges.copy()
    cv2.floodFill(im_floodfill, glove_mask, (0, 0), 255)
    cv2.drawContours(glove_mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
    # Bitwise AND to obtain the segmented glove region
    # segmented_glove = cv2.bitwise_and(image, image, mask=glove_mask)
    # Display the results
    cv2.imshow('Original Image', image)
    cv2.imshow("Edges", edges)
    cv2.imshow('Floodfilled image', im_floodfill)
    # cv2.imshow('Segmented Glove', segmented_glove)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def segment_glove_thresholding(rgb_image, kernel_blur, kernel_opening_size, lower_thres, upper_thres, contrast, brightness):
    rgb_image_copy = cv2.convertScaleAbs(rgb_image, alpha=contrast, beta=brightness)
    rgb_image_converted = cv2.convertScaleAbs(rgb_image, alpha=contrast, beta=brightness)
    gray_image = cv2.cvtColor(rgb_image_converted, cv2.COLOR_BGR2GRAY)
    kernel_opening = np.ones((kernel_opening_size, kernel_opening_size), np.uint8)
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
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# segment_glove_canny(img1, 7, 0, 253)
# segment_glove_canny(img2, 7, 0, 253)
segment_glove_thresholding(img1, 7, 0, 241, 255, 2, -10)
segment_glove_thresholding(img2, 7, 0, 241, 255, 2, -10)

