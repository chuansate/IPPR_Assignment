"""
Here to run the GUI I guess?
Before GUI, we run CLI here!
"""
from tuning_utils import *
from algorithms import *
medicalGlove1 = cv2.imread("Glove_images/medical/dirty_and_stain/dirty_and_stain_1.jpeg")
medicalGlove2 = cv2.imread("Glove_images/medical/dirty_and_stain/dirty_and_stain_2.jpeg")
medicalGlove3 = cv2.imread("Glove_images/medical/dirty_and_stain/dirty_and_stain_3.jpeg")
nitrileGlove1 = cv2.imread("Glove_images/nitrile/HOLE/NITRILE HOLE 1.jpg")
nitrileGlove2 = cv2.imread("Glove_images/nitrile/HOLE/NITRILE HOLE 2.jpg")
siliconeGlove1 = cv2.imread("Glove_images/silicone/mould/mould_1.jpeg")
siliconeGlove2 = cv2.imread("Glove_images/silicone/mould/mould_2.jpeg")
# DUN USE FABRIC GLOVE!!
# fabric glove is in white, and the medical glove's background is in white too, hence medical glove will be recognized as fabric!
# fabricGlove1 = cv2.imread("Glove_images/Fabric_gloves/stain/CLOTH STAIN 1.jpg")
# fabricGlove2 = cv2.imread("Glove_images/Fabric_gloves/stain/CLOTH STAIN 2.jpg")

totalGloveType = 3


def main():
    print(identifyGloveType(medicalGlove1, totalGloveType))
    print(identifyGloveType(medicalGlove2, totalGloveType))
    print(identifyGloveType(medicalGlove3, totalGloveType))
    print(identifyGloveType(nitrileGlove1, totalGloveType))
    print(identifyGloveType(nitrileGlove2, totalGloveType))
    print(identifyGloveType(siliconeGlove1, totalGloveType))
    print(identifyGloveType(siliconeGlove2, totalGloveType))


if __name__ == "__main__":
    main()