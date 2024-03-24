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
nitrileGlove3 = cv2.imread("Glove_images/nitrile/mix/NITRILE MIX 1.jpg")
nitrileGlove4 = cv2.imread("Glove_images/nitrile/mix/NITRILE MIX 2.jpg")
nitrileGlove5 = cv2.imread("Glove_images/nitrile/fingertip_hole/NITRILE FINGER HOLE 1.jpg")
nitrileGlove6 = cv2.imread("Glove_images/nitrile/fingertip_hole/NITRILE FINGER HOLE 2.jpg")
siliconeGlove1 = cv2.imread("Glove_images/silicone/mould/mould_1.jpeg")
siliconeGlove2 = cv2.imread("Glove_images/silicone/mould/mould_2.jpeg")
siliconeGlove3 = cv2.imread("Glove_images/silicone/mould/mould_3.jpeg")
fabricGlove1 = cv2.imread("Glove_images/fabric/opening/opening1.jpg")
fabricGlove2 = cv2.imread("Glove_images/fabric/opening/opening2.jpg")
fabricGlove3 = cv2.imread("Glove_images/fabric/stitch/CLOTH STITCH 2.jpg")
fabricGlove4 = cv2.imread("Glove_images/fabric/multiple_stains/multiple_stains2.jpg")
fabricGlove5 = cv2.imread("Glove_images/fabric/stitch/CLOTH STITCH 2.jpg")
fabricGlove6 = cv2.imread("Glove_images/fabric/stitch/CLOTH STITCH 3.jpg")
totalGloveType = 4

def identifyDefectType(img, gloveTypeName):
    if gloveTypeName == "medical glove":
        identifyDefectType_MedicalGlove(img, minDirtyArea=1420, maxDirtyArea=1450, minPartialTearArea=620, maxPartialTearArea=625, minDirtyEcc=0.54, maxDirtyEcc=0.58, minPartialTearEcc=0.43, maxPartialTearEcc=0.48)
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

    print(identifyGloveType(nitrileGlove2, totalGloveType))
    cv2.putText(fabricGlove1, 'Glove Type = Nitrile glove', (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("Glove", fabricGlove1)
    cv2.waitKey(0)
    # print glove types
    # print(identifyGloveType(medicalGlove1, totalGloveType))
    # print(identifyGloveType(medicalGlove2, totalGloveType))
    # print(identifyGloveType(nitrileGlove1, totalGloveType))
    # print(identifyGloveType(nitrileGlove2, totalGloveType))
    # print(identifyGloveType(siliconeGlove1, totalGloveType))
    # print(identifyGloveType(siliconeGlove2, totalGloveType))
    # print(identifyGloveType(siliconeGlove3, totalGloveType))
    # print(identifyGloveType(fabricGlove1, totalGloveType))
    # print(identifyGloveType(fabricGlove2, totalGloveType))
    # print(identifyGloveType(fabricGlove3, totalGloveType))
    # print(identifyGloveType(fabricGlove4, totalGloveType))
    # print(identifyGloveType(fabricGlove5, totalGloveType))
    # print(identifyGloveType(fabricGlove6, totalGloveType))

    identifyDefectType_FabricGlove(fabricGlove1, 120, 1300, 1400)
    identifyDefectType_FabricGlove(fabricGlove2, 140, 300, 1500)
    identifyDefectType_FabricGlove(fabricGlove3, 140, 200, 1100)
    identifyDefectType_FabricGlove(fabricGlove4, 150, 100, 900)
    identifyDefectType_FabricGlove(fabricGlove5, 70, 100, 200)
    identifyDefectType_FabricGlove(fabricGlove6, 60, 100, 200)

if __name__ == "__main__":
    main()
