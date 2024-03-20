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


def identifyDefectType(img, gloveTypeName):
    if gloveTypeName == "medical glove":
        identifyDefectType_MedicalGlove(img, minDirtyArea=1420, maxDirtyArea=1450, minPartialTearArea=620, maxPartialTearArea=625)
    elif gloveTypeName == "nitrile glove":
        pass
    elif gloveTypeName == "silicone glove":
        pass
    elif gloveTypeName == "fabric glove":
        pass
    else:
        print("Unknown glove type!")


def main():
    gloveTypeName1 = identifyGloveType(medicalGlove1, totalGloveType)
    identifyDefectType(medicalGlove1, gloveTypeName1)

    gloveTypeName2 = identifyGloveType(medicalGlove2, totalGloveType)
    identifyDefectType(medicalGlove2, gloveTypeName2)

    gloveTypeName3 = identifyGloveType(medicalGlove3, totalGloveType)
    identifyDefectType(medicalGlove3, gloveTypeName3)

    gloveTypeName4 = identifyGloveType(medicalGlove4, totalGloveType)
    identifyDefectType(medicalGlove4, gloveTypeName4)

    gloveTypeName5 = identifyGloveType(medicalGlove5, totalGloveType)
    identifyDefectType(medicalGlove5, gloveTypeName5)

    gloveTypeName6 = identifyGloveType(medicalGlove6, totalGloveType)
    identifyDefectType(medicalGlove6, gloveTypeName6)


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
