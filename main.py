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
fabricGlove1 = cv2.imread("Glove_images/fabric/opening/opening1.jpg")
fabricGlove2 = cv2.imread("Glove_images/fabric/opening/opening2.jpg")
fabricGlove3 = cv2.imread("Glove_images/fabric/stitch/CLOTH STITCH 2.jpg")
fabricGlove4 = cv2.imread("Glove_images/fabric/multiple_stains/multiple_stains2.jpg")
fabricGlove5 = cv2.imread("Glove_images/fabric/stitch/CLOTH STITCH 2.jpg")
fabricGlove6 = cv2.imread("Glove_images/fabric/stitch/CLOTH STITCH 3.jpg")
totalGloveType = 4
totalGloveType_nitrile = 1

# helper function for identifying the defect type on the medical gloves
def identifyDefectType_MedicalGlove_HelperFunc(img):
    identifyDefectType_MedicalGlove(img, minDirtyArea=1420, maxDirtyArea=1450, minPartialTearArea=620, maxPartialTearArea=625, minDirtyEcc=0.54, maxDirtyEcc=0.58, minPartialTearEcc=0.43, maxPartialTearEcc=0.48)


def main():
    # identification of glove type
    ## medical gloves
    identifyGloveType(medicalGlove1, totalGloveType)
    identifyGloveType(medicalGlove2, totalGloveType)
    identifyGloveType(medicalGlove3, totalGloveType)
    identifyGloveType(medicalGlove4, totalGloveType)
    identifyGloveType(medicalGlove5, totalGloveType)
    identifyGloveType(medicalGlove6, totalGloveType)
    ## fabric gloves
    identifyGloveType(fabricGlove1, totalGloveType)
    identifyGloveType(fabricGlove2, totalGloveType)
    identifyGloveType(fabricGlove3, totalGloveType)
    identifyGloveType(fabricGlove4, totalGloveType)
    identifyGloveType(fabricGlove5, totalGloveType)
    identifyGloveType(fabricGlove6, totalGloveType)

    ## silicone gloves
    identifyGloveType(siliconeGlove1, totalGloveType)
    identifyGloveType(siliconeGlove2, totalGloveType)
    identifyGloveType(siliconeGlove3, totalGloveType)
    identifyGloveType(siliconeGlove4, totalGloveType)
    identifyGloveType(siliconeGlove5, totalGloveType)
    identifyGloveType(siliconeGlove6, totalGloveType)
    identifyGloveType(siliconeGlove7, totalGloveType)
    identifyGloveType(siliconeGlove8, totalGloveType)
    identifyGloveType(siliconeGlove9, totalGloveType)
    identifyGloveType(siliconeGlove10, totalGloveType)
    identifyGloveType(siliconeGlove11, totalGloveType)
    identifyGloveType(siliconeGlove12, totalGloveType)
    identifyGloveType(siliconeGlove13, totalGloveType)
    identifyGloveType(siliconeGlove14, totalGloveType)
    identifyGloveType(siliconeGlove15, totalGloveType)

    ## nitrile gloves
    identifyGloveType(nitrileGlove1, totalGloveType)
    identifyGloveType(nitrileGlove2, totalGloveType)
    identifyGloveType(nitrileGlove3, totalGloveType)
    identifyGloveType(nitrileGlove4, totalGloveType)
    identifyGloveType(nitrileGlove5, totalGloveType)
    identifyGloveType(nitrileGlove6, totalGloveType)
    identifyGloveType(nitrileGlove7, totalGloveType)
    identifyGloveType(nitrileGlove8, totalGloveType)
    identifyGloveType(nitrileGlove9, totalGloveType)
    identifyGloveType(nitrileGlove10, totalGloveType)

    # identification of defect types
    ## medical glove
    identifyDefectType_MedicalGlove_HelperFunc(medicalGlove1)
    identifyDefectType_MedicalGlove_HelperFunc(medicalGlove2)
    identifyDefectType_MedicalGlove_HelperFunc(medicalGlove3)
    identifyDefectType_MedicalGlove_HelperFunc(medicalGlove4)
    identifyDefectType_MedicalGlove_HelperFunc(medicalGlove5)
    identifyDefectType_MedicalGlove_HelperFunc(medicalGlove6)

    # silicone glove
    print(identifyGloveType(siliconeGlove1, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove1)
    print(identifyGloveType(siliconeGlove2, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove2)
    print(identifyGloveType(siliconeGlove3, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove3)
    print(identifyGloveType(siliconeGlove4, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove4)
    print(identifyGloveType(siliconeGlove5, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove5)
    print(identifyGloveType(siliconeGlove6, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove6)
    print(identifyGloveType(siliconeGlove7, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove7)
    print(identifyGloveType(siliconeGlove8, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove8)
    print(identifyGloveType(siliconeGlove9, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove9)
    print(identifyGloveType(siliconeGlove10, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove10)
    print(identifyGloveType(siliconeGlove11, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove11)
    print(identifyGloveType(siliconeGlove12, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove12)
    print(identifyGloveType(siliconeGlove13, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove13)
    print(identifyGloveType(siliconeGlove14, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove14)
    print(identifyGloveType(siliconeGlove15, totalGloveType))
    identifyDefectType_SiliconeGlove(siliconeGlove15)


    # fabric glove
    identifyDefectType_FabricGlove(fabricGlove1, 120, 1300, 1400)
    identifyDefectType_FabricGlove(fabricGlove2, 140, 300, 1500)
    identifyDefectType_FabricGlove(fabricGlove3, 140, 200, 1100)
    identifyDefectType_FabricGlove(fabricGlove4, 150, 100, 900)
    identifyDefectType_FabricGlove(fabricGlove5, 70, 100, 200)
    identifyDefectType_FabricGlove(fabricGlove6, 60, 100, 200)

    # nitrile glove
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


def main_GUI():
    # 2 buttons: identify the glove type, and identify the defect type
    pass

if __name__ == "__main__":
    main()