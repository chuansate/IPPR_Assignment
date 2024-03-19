"""
Here to run the GUI I guess?
Before GUI, we run CLI here!
"""
from tuning_utils import *
from algorithms import *
medicalGlove1 = cv2.imread("Glove_images/medical/dirty_and_stain/dirty_and_stain_1.jpeg")
medicalGlove2 = cv2.imread("Glove_images/medical/dirty_and_stain/dirty_and_stain_2.jpeg")
medicalGlove3 = cv2.imread("Glove_images/medical/dirty_and_stain/dirty_and_stain_3.jpeg")
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
    print(identifyGloveType(medicalGlove2, totalGloveType))
    print(identifyGloveType(medicalGlove3, totalGloveType))
    print(identifyGloveType(nitrileGlove1, totalGloveType))
    print(identifyGloveType(nitrileGlove2, totalGloveType))
    print(identifyGloveType(nitrileGlove3, totalGloveType))
    print(identifyGloveType(nitrileGlove4, totalGloveType))
    print(identifyGloveType(siliconeGlove1, totalGloveType))
    print(identifyGloveType(siliconeGlove2, totalGloveType))

    holes_in_nitrile_glove1 = identify_fingertipholes_in_glove(nitrileGlove1)
    print(f"Detected {len(holes_in_nitrile_glove1)} holes in nitrileGlove1.")

    holes_in_nitrile_glove2 = identify_fingertipholes_in_glove(nitrileGlove2)
    print(f"Detected {len(holes_in_nitrile_glove2)} holes in nitrileGlove2.")

    holes_in_nitrile_glove3 = identify_fingertipholes_in_glove(nitrileGlove3)
    print(f"Detected {len(holes_in_nitrile_glove3)} holes in nitrileGlove3.")

    # After identifying the glove type, check for fingertip stains if it's a nitrile glove
    # Example for one image:
    gloveType = identifyGloveType(nitrileGlove1, totalGloveType)
    if gloveType == "nitrile glove":
        defects_info = identifyStain(gloveType, nitrileGlove1)
        print(defects_info)
    # Do the same for all other images

    # Add to main.py within the main() function

    # Add the HSV range for black or the color of the holes/background
    hsv_lower_holes = (0, 0, 0)
    hsv_upper_holes = (180, 255, 30)  # Adjust this based on your actual background color

    # Assume that the identify_holes function is already imported
    # Call the identify_holes function for each nitrile glove image
    mask, holes = identify_holes(nitrileGlove1, hsv_lower_holes, hsv_upper_holes)
    # Do something with the mask and holes, like counting them or highlighting them


if __name__ == "__main__":
    main()