"""
Here to run the GUI I guess?
Before GUI, we run CLI here!
"""
from tuning_utils import *
from algorithms import *
medicalGlove1 = cv2.imread("Glove_images/medical/dirty/dirty1.jpeg")
medicalGlove2 = cv2.imread("Glove_images/medical/dirty/dirty2.jpeg")
nitrileGlove1 = cv2.imread("Glove_images/nitrile/stain/NITRILE STAIN 1.jpg")
nitrileGlove2 = cv2.imread("Glove_images/nitrile/stain/NITRILE STAIN 2.jpg")
siliconeGlove1 = cv2.imread("Glove_images/silicone/mould/mould_1.jpeg")
siliconeGlove2 = cv2.imread("Glove_images/silicone/mould/mould_2.jpeg")
siliconeGlove3 = cv2.imread("Glove_images/silicone/mould/mould_3.jpeg")
siliconeGlove4 = cv2.imread("Glove_images/silicone/mould/mould_4.jpeg")
siliconeGlove5 = cv2.imread("Glove_images/silicone/mould/mould_5.jpeg")
siliconeGlove6 = cv2.imread("Glove_images/silicone/mark/mark1.jpeg")
siliconeGlove7 = cv2.imread("Glove_images/silicone/mark/mark2.jpeg")
siliconeGlove8 = cv2.imread("Glove_images/silicone/mark/mark3.jpeg")
siliconeGlove9 = cv2.imread("Glove_images/silicone/mark/mark4.jpeg")
siliconeGlove10 = cv2.imread("Glove_images/silicone/mark/mark5.jpeg")
siliconeGlove11 = cv2.imread("Glove_images/silicone/missing_finger/missing_finger_1.jpeg")
siliconeGlove12 = cv2.imread("Glove_images/silicone/missing_finger/missing_finger_2.jpeg")
siliconeGlove13 = cv2.imread("Glove_images/silicone/missing_finger/missing_finger_3.jpeg")
siliconeGlove14 = cv2.imread("Glove_images/silicone/missing_finger/missing_finger_4.jpeg")
siliconeGlove15 = cv2.imread("Glove_images/silicone/missing_finger/missing_finger_5.jpeg")
fabricGlove1 = cv2.imread("Glove_images/fabric/multiple_stains/mark1.jpeg")
fabricGlove2 = cv2.imread("Glove_images/fabric/multiple_stains/multiple_stains2.jpg")

totalGloveType = 4


def main():
    # detectGloveTrackbar(siliconeGlove1)
    detectGloveDefectType(siliconeGlove1)
    detectGloveDefectType(siliconeGlove2)
    detectGloveDefectType(siliconeGlove3)
    detectGloveDefectType(siliconeGlove4)
    detectGloveDefectType(siliconeGlove5)
    detectGloveDefectType(siliconeGlove6)
    detectGloveDefectType(siliconeGlove7)
    detectGloveDefectType(siliconeGlove8)
    detectGloveDefectType(siliconeGlove9)
    detectGloveDefectType(siliconeGlove10)
    detectGloveDefectType(siliconeGlove11)
    detectGloveDefectType(siliconeGlove12)
    detectGloveDefectType(siliconeGlove13)
    detectGloveDefectType(siliconeGlove14)
    detectGloveDefectType(siliconeGlove15)



if __name__ == "__main__":
    main()