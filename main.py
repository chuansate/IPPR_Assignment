"""
Here to run the GUI I guess?
Before GUI, we run CLI here!
"""
from tuning_utils import *
from algorithms import *
import cv2

medicalGlove1 = cv2.imread("Glove_images/medical/dirty/dirty1.jpeg")
medicalGlove2 = cv2.imread("Glove_images/medical/dirty/dirty2.jpeg")
medicalGlove3 = cv2.imread("Glove_images/medical/fingertip_tear/fingertip_tear1.jpeg")
medicalGlove4 = cv2.imread("Glove_images/medical/fingertip_tear/fingertip_tear2.jpeg")
medicalGlove5 = cv2.imread("Glove_images/medical/partial_tear/partial_tear1.jpeg")
medicalGlove6 = cv2.imread("Glove_images/medical/partial_tear/partial_tear2.jpeg")
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

totalGloveType = 4

totalGloveType_nitrile = 1


def identifyDefectType(img, gloveTypeName):
    if gloveTypeName == "medical glove":
       pass
    elif gloveTypeName == "nitrile glove":
       identifyDefectTypes_NitrileGlove(img)
    elif gloveTypeName == "silicone glove":
        pass
    elif gloveTypeName == "fabric glove":
        pass
    else:
        print("Unknown glove type!")


def main():

    gloveTypeName7 = identifyGloveType_nitrile(nitrileGlove1, totalGloveType_nitrile)
    identifyDefectType(nitrileGlove1, gloveTypeName7)

    gloveTypeName8 = identifyGloveType_nitrile(nitrileGlove2, totalGloveType_nitrile)
    identifyDefectType(nitrileGlove2, gloveTypeName8)

    gloveTypeName9 = identifyGloveType_nitrile(nitrileGlove3, totalGloveType_nitrile)
    identifyDefectType(nitrileGlove3, gloveTypeName9)

    gloveTypeName10 = identifyGloveType_nitrile(nitrileGlove4, totalGloveType_nitrile)
    identifyDefectType(nitrileGlove4, gloveTypeName10)

    gloveTypeName11 = identifyGloveType_nitrile(nitrileGlove5, totalGloveType_nitrile)
    identifyDefectType(nitrileGlove5, gloveTypeName11)

    gloveTypeName12 = identifyGloveType_nitrile(nitrileGlove6, totalGloveType_nitrile)
    identifyDefectType(nitrileGlove6, gloveTypeName12)

    gloveTypeName13 = identifyGloveType_nitrile(nitrileGlove7, totalGloveType_nitrile)
    identifyDefectType(nitrileGlove7, gloveTypeName13)

    gloveTypeName14 = identifyGloveType_nitrile(nitrileGlove8, totalGloveType_nitrile)
    identifyDefectType(nitrileGlove8, gloveTypeName14)

    gloveTypeName15 = identifyGloveType_nitrile(nitrileGlove9, totalGloveType_nitrile)
    identifyDefectType(nitrileGlove9, gloveTypeName15)

    gloveTypeName16 = identifyGloveType_nitrile(nitrileGlove10, totalGloveType_nitrile)
    identifyDefectType(nitrileGlove10, gloveTypeName16)


    # print(identifyGloveType(medicalGlove3, totalGloveType))
    # identifyDefectType_MedicalGlove(medicalGlove3)
    # print(identifyGloveType(medicalGlove4, totalGloveType))
    # identifyDefectType_MedicalGlove(medicalGlove4)
    # print(identifyGloveType(medicalGlove5, totalGloveType))
    # identifyDefectType_MedicalGlove(medicalGlove5)
    # print(identifyGloveType(medicalGlove6, totalGloveType))
    # identifyDefectType_MedicalGlove(medicalGlove6)


if __name__ == "__main__":
    main()
