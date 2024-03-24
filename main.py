"""
Here to run the GUI I guess?
Before GUI, we run CLI here!
"""
from tuning_utils import *
from algorithms import *
medicalGlove1 = cv2.imread("Glove_images/medical/dirty/dirty1.jpeg")
medicalGlove2 = cv2.imread("Glove_images/medical/dirty/dirty2.jpeg")
nitrileGlove1 = cv2.imread("Glove_images/nitrile/fingertip_hole/NITRILE STAIN 1.jpg")
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

def main():
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