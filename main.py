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
fabricGlove1 = cv2.imread("Glove_images/fabric/multiple_stains/multiple_stains1.jpg")
fabricGlove2 = cv2.imread("Glove_images/fabric/multiple_stains/multiple_stains2.jpg")

totalGloveType = 4


def main():
    print(identifyGloveType(medicalGlove1, totalGloveType))
    print(identifyGloveType(medicalGlove2, totalGloveType))
    print(identifyGloveType(nitrileGlove1, totalGloveType))
    print(identifyGloveType(nitrileGlove2, totalGloveType))
    print(identifyGloveType(siliconeGlove1, totalGloveType))
    print(identifyGloveType(siliconeGlove2, totalGloveType))
    print(identifyGloveType(siliconeGlove3, totalGloveType))
    print(identifyGloveType(fabricGlove1, totalGloveType))
    print(identifyGloveType(fabricGlove2, totalGloveType))


if __name__ == "__main__":
    main()