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

def identifyDefectType(img, gloveTypeName):
    if gloveTypeName == "medical glove":
        identifyDefectType_MedicalGlove(img, minDirtyArea=1420, maxDirtyArea=1450, minPartialTearArea=620, maxPartialTearArea=625, minDirtyEcc=0.54, maxDirtyEcc=0.58, minPartialTearEcc=0.43, maxPartialTearEcc=0.48)
    elif gloveTypeName == "nitrile glove":
       identifyDefectTypes_NitrileGlove(img)
    elif gloveTypeName == "silicone glove":
        pass
    elif gloveTypeName == "fabric glove":
        pass
    else:
        print("Unknown glove type!")

def main():
    # medical glove
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

    print(identifyGloveType(nitrileGlove2, totalGloveType))
    cv2.putText(fabricGlove1, 'Glove Type = Nitrile glove', (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("Glove", fabricGlove1)
    cv2.waitKey(0)

    # fabric glove
    identifyDefectType_FabricGlove(fabricGlove1, 120, 1300, 1400)
    identifyDefectType_FabricGlove(fabricGlove2, 140, 300, 1500)
    identifyDefectType_FabricGlove(fabricGlove3, 140, 200, 1100)
    identifyDefectType_FabricGlove(fabricGlove4, 150, 100, 900)
    identifyDefectType_FabricGlove(fabricGlove5, 70, 100, 200)
    identifyDefectType_FabricGlove(fabricGlove6, 60, 100, 200)

    # silicone glove
    detectGloveDefectType_SiliconGlove(siliconeGlove1)
    detectGloveDefectType_SiliconGlove(siliconeGlove2)
    detectGloveDefectType_SiliconGlove(siliconeGlove3)
    detectGloveDefectType_SiliconGlove(siliconeGlove4)
    detectGloveDefectType_SiliconGlove(siliconeGlove5)
    detectGloveDefectType_SiliconGlove(siliconeGlove6)
    detectGloveDefectType_SiliconGlove(siliconeGlove7)
    detectGloveDefectType_SiliconGlove(siliconeGlove8)
    detectGloveDefectType_SiliconGlove(siliconeGlove9)
    detectGloveDefectType_SiliconGlove(siliconeGlove10)
    detectGloveDefectType_SiliconGlove(siliconeGlove11)
    detectGloveDefectType_SiliconGlove(siliconeGlove12)
    detectGloveDefectType_SiliconGlove(siliconeGlove13)
    detectGloveDefectType_SiliconGlove(siliconeGlove14)
    detectGloveDefectType_SiliconGlove(siliconeGlove15)

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

if __name__ == "__main__":
    main()