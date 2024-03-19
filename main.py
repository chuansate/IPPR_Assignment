"""
Here to run the GUI I guess?
Before GUI, we run CLI here!
"""
from tuning_utils import *
from algorithms import *
medicalGlove1 = cv2.imread("Glove_images/medical/dirty/dirty1.jpeg")
medicalGlove2 = cv2.imread("Glove_images/medical/dirty/dirty2.jpeg")
medicalGlove3 = cv2.imread("Glove_images/medical/fingertip_tear/fingertip_tear1.jpeg")
medicalGlove4 = cv2.imread("Glove_images/medical/fingertip_tear/fingertip_tear2.jpeg")
medicalGlove5 = cv2.imread("Glove_images/medical/partial_tear/partial_tear1.jpeg")
medicalGlove6 = cv2.imread("Glove_images/medical/partial_tear/partial_tear2.jpeg")
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
    print(identifyDefectType_MedicalGlove(medicalGlove1, minDirtyArea=1420, maxDirtyArea=1450, minPartialTearArea=620,
                                    maxPartialTearArea=625))
    print()
    print(identifyGloveType(medicalGlove2, totalGloveType))
    print(identifyDefectType_MedicalGlove(medicalGlove2, minDirtyArea=1420, maxDirtyArea=1450, minPartialTearArea=620,
                                    maxPartialTearArea=625))
    print()
    print(identifyGloveType(medicalGlove3, totalGloveType))
    print(identifyDefectType_MedicalGlove(medicalGlove3, minDirtyArea=1420, maxDirtyArea=1450, minPartialTearArea=620,
                                    maxPartialTearArea=625))
    print()
    print(identifyGloveType(medicalGlove4, totalGloveType))
    print(identifyDefectType_MedicalGlove(medicalGlove4, minDirtyArea=1420, maxDirtyArea=1450, minPartialTearArea=620,
                                    maxPartialTearArea=625))
    print()
    print(identifyGloveType(medicalGlove5, totalGloveType))
    print(identifyDefectType_MedicalGlove(medicalGlove5, minDirtyArea=1420, maxDirtyArea=1450, minPartialTearArea=620, maxPartialTearArea=625))
    print()
    print(identifyGloveType(medicalGlove6, totalGloveType))
    print(identifyDefectType_MedicalGlove(medicalGlove6, minDirtyArea=1420, maxDirtyArea=1450, minPartialTearArea=620, maxPartialTearArea=625))
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
