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
    print(identifyGloveType(medicalGlove1, totalGloveType))
    print(identifyGloveType(medicalGlove2, totalGloveType))
    print(identifyGloveType(medicalGlove3, totalGloveType))
    print(identifyGloveType(medicalGlove4, totalGloveType))
    print(identifyGloveType(medicalGlove5, totalGloveType))
    print(identifyGloveType(medicalGlove6, totalGloveType))
    ## fabric gloves
    print(identifyGloveType(fabricGlove1, totalGloveType))
    print(identifyGloveType(fabricGlove2, totalGloveType))
    print(identifyGloveType(fabricGlove3, totalGloveType))
    print(identifyGloveType(fabricGlove4, totalGloveType))
    print(identifyGloveType(fabricGlove5, totalGloveType))
    print(identifyGloveType(fabricGlove6, totalGloveType))

    ## silicone gloves
    print(identifyGloveType(siliconeGlove1, totalGloveType))
    print(identifyGloveType(siliconeGlove2, totalGloveType))
    print(identifyGloveType(siliconeGlove3, totalGloveType))
    print(identifyGloveType(siliconeGlove4, totalGloveType))
    print(identifyGloveType(siliconeGlove5, totalGloveType))
    print(identifyGloveType(siliconeGlove6, totalGloveType))
    print(identifyGloveType(siliconeGlove7, totalGloveType))
    print(identifyGloveType(siliconeGlove8, totalGloveType))
    print(identifyGloveType(siliconeGlove9, totalGloveType))
    print(identifyGloveType(siliconeGlove10, totalGloveType))
    print(identifyGloveType(siliconeGlove11, totalGloveType))
    print(identifyGloveType(siliconeGlove12, totalGloveType))
    print(identifyGloveType(siliconeGlove13, totalGloveType))
    print(identifyGloveType(siliconeGlove14, totalGloveType))
    print(identifyGloveType(siliconeGlove15, totalGloveType))

    ## nitrile gloves
    print(identifyGloveType(nitrileGlove1, totalGloveType))
    print(identifyGloveType(nitrileGlove2, totalGloveType))
    print(identifyGloveType(nitrileGlove3, totalGloveType))
    print(identifyGloveType(nitrileGlove4, totalGloveType))
    print(identifyGloveType(nitrileGlove5, totalGloveType))
    print(identifyGloveType(nitrileGlove6, totalGloveType))
    print(identifyGloveType(nitrileGlove7, totalGloveType))
    print(identifyGloveType(nitrileGlove8, totalGloveType))
    print(identifyGloveType(nitrileGlove9, totalGloveType))
    print(identifyGloveType(nitrileGlove10, totalGloveType))
    print("Identification of glove type ends here!")

    # identification of defect types
    ## medical glove
    identifyDefectType_MedicalGlove_HelperFunc(medicalGlove1)
    identifyDefectType_MedicalGlove_HelperFunc(medicalGlove2)
    identifyDefectType_MedicalGlove_HelperFunc(medicalGlove3)
    identifyDefectType_MedicalGlove_HelperFunc(medicalGlove4)
    identifyDefectType_MedicalGlove_HelperFunc(medicalGlove5)
    identifyDefectType_MedicalGlove_HelperFunc(medicalGlove6)

    # silicone glove
    identifyDefectType_SiliconeGlove(siliconeGlove1)
    identifyDefectType_SiliconeGlove(siliconeGlove2)
    identifyDefectType_SiliconeGlove(siliconeGlove3)
    identifyDefectType_SiliconeGlove(siliconeGlove4)
    identifyDefectType_SiliconeGlove(siliconeGlove5)
    identifyDefectType_SiliconeGlove(siliconeGlove6)
    identifyDefectType_SiliconeGlove(siliconeGlove7)
    identifyDefectType_SiliconeGlove(siliconeGlove8)
    identifyDefectType_SiliconeGlove(siliconeGlove9)
    identifyDefectType_SiliconeGlove(siliconeGlove10)
    identifyDefectType_SiliconeGlove(siliconeGlove11)
    identifyDefectType_SiliconeGlove(siliconeGlove12)
    identifyDefectType_SiliconeGlove(siliconeGlove13)
    identifyDefectType_SiliconeGlove(siliconeGlove14)
    identifyDefectType_SiliconeGlove(siliconeGlove15)

    # fabric glove
    identifyDefectType_FabricGlove(fabricGlove1, 120, 1300, 1400)
    identifyDefectType_FabricGlove(fabricGlove2, 140, 300, 1500)
    identifyDefectType_FabricGlove(fabricGlove3, 140, 200, 1100)
    identifyDefectType_FabricGlove(fabricGlove4, 150, 100, 900)
    identifyDefectType_FabricGlove(fabricGlove5, 70, 100, 200)
    identifyDefectType_FabricGlove(fabricGlove6, 60, 100, 200)

    # nitrile glove
    identifyDefectTypes_NitrileGlove(nitrileGlove1)
    identifyDefectTypes_NitrileGlove(nitrileGlove2)
    identifyDefectTypes_NitrileGlove(nitrileGlove3)
    identifyDefectTypes_NitrileGlove(nitrileGlove4)
    identifyDefectTypes_NitrileGlove(nitrileGlove5)
    identifyDefectTypes_NitrileGlove(nitrileGlove6)
    identifyDefectTypes_NitrileGlove(nitrileGlove7)
    identifyDefectTypes_NitrileGlove(nitrileGlove8)
    identifyDefectTypes_NitrileGlove(nitrileGlove9)
    identifyDefectTypes_NitrileGlove(nitrileGlove10)


def main_GUI():
    # 2 buttons: identify the glove type, and identify the defect type
    pass


if __name__ == "__main__":
    main()