"""
Here to run the GUI I guess?
Before GUI, we run CLI here!
"""
from tuning_utils import *
from algorithms import *
medicalGlove1 = cv2.imread("Glove_images/medical/dirty_and_stain/dirty_and_stain_1.jpeg")
medicalGlove2 = cv2.imread("Glove_images/medical/dirty_and_stain/dirty_and_stain_2.jpeg")
medicalGlove3 = cv2.imread("Glove_images/medical/hole/hole_1.jpeg")
medicalGlove4 = cv2.imread("Glove_images/medical/hole/hole_2.jpeg")
medicalGlove5 = cv2.imread("Glove_images/medical/missing_finger/missing_finger_1.jpeg")
medicalGlove6 = cv2.imread("Glove_images/medical/missing_finger/missing_finger_2.jpeg")
nitrileGlove1 = cv2.imread("Glove_images/nitrile/STAIN/NITRILE STAIN 1.jpg")
nitrileGlove2 = cv2.imread("Glove_images/nitrile/STAIN/NITRILE STAIN 2.jpg")
nitrileGlove3 = cv2.imread("Glove_images/nitrile/HOLE/NITRILE HOLE 1.jpg")
nitrileGlove4 = cv2.imread("Glove_images/nitrile/HOLE/NITRILE HOLE 2.jpg")

siliconeGlove1 = cv2.imread("Glove_images/silicone/mould/mould_1.jpeg")
siliconeGlove2 = cv2.imread("Glove_images/silicone/mould/mould_2.jpeg")
# DUN USE FABRIC GLOVE!!
# fabric glove is in white, and the medical glove's background is in white too, hence medical glove will be recognized as fabric!
# fabricGlove1 = cv2.imread("Glove_images/Fabric_gloves/stain/CLOTH STAIN 1.jpg")
# fabricGlove2 = cv2.imread("Glove_images/Fabric_gloves/stain/CLOTH STAIN 2.jpg")

totalGloveType = 3


def main():
    print(identifyGloveType(medicalGlove1, totalGloveType))
    identifyDefectType_MedicalGlove(medicalGlove1)
    print(identifyGloveType(medicalGlove2, totalGloveType))
    identifyDefectType_MedicalGlove(medicalGlove2)
    print(identifyGloveType(medicalGlove3, totalGloveType))
    identifyDefectType_MedicalGlove(medicalGlove3)
    print(identifyGloveType(medicalGlove4, totalGloveType))
    identifyDefectType_MedicalGlove(medicalGlove4)
    print(identifyGloveType(medicalGlove5, totalGloveType))
    identifyDefectType_MedicalGlove(medicalGlove5)
    print(identifyGloveType(medicalGlove6, totalGloveType))
    identifyDefectType_MedicalGlove(medicalGlove6)

    # print(identifyGloveType(medicalGlove1, totalGloveType))
    # print(identifyGloveType(medicalGlove2, totalGloveType))
    # print(identifyGloveType(medicalGlove3, totalGloveType))
    # print(identifyGloveType(medicalGlove4, totalGloveType))
    # print(identifyGloveType(medicalGlove5, totalGloveType))
    # print(identifyGloveType(medicalGlove6, totalGloveType))
    # print(identifyGloveType(nitrileGlove1, totalGloveType))
    # print(identifyGloveType(nitrileGlove2, totalGloveType))
    # print(identifyGloveType(nitrileGlove3, totalGloveType))
    # print(identifyGloveType(nitrileGlove4, totalGloveType))
    # print(identifyGloveType(siliconeGlove1, totalGloveType))
    # print(identifyGloveType(siliconeGlove2, totalGloveType))


if __name__ == "__main__":
    main()
