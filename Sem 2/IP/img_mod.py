#from statistics import correlation
from PIL import Image
from PIL import ImageFilter
import numpy as np

def negImg():
    original = Image.open("/home/jerinpaul/Pictures/wolf.jpg")
    img = Image.open("/home/jerinpaul/Pictures/wolf.jpg")
    for i in range(0, img.size[0] - 1):
        for j in range(0, img.size[1] - 1):
            pixelColorVals = img.getpixel((i,j))
            redPixel = 255 - pixelColorVals[0]
            greenPixel = 255 - pixelColorVals[1]
            bluePixel = 255 - pixelColorVals[2]
            img.putpixel((i,j),(redPixel, greenPixel, bluePixel))
    original.show()
    img.show()

def contStretch():
    imageObject = Image.open("/home/jerinpaul/Pictures/medow.jpg")
    multiBands = imageObject.split()
    normalizedRedBand = multiBands[0].point(normalizeRed)
    normalizedGreenBand = multiBands[1].point(normalizeGreen)
    normalizedBlueBand = multiBands[2].point(normalizeBlue)
    normalizedImage = Image.merge("RGB", (normalizedRedBand, normalizedGreenBand, normalizedBlueBand))
    imageObject.show()
    normalizedImage.show()

def normalizeRed(intensity):
    iI = intensity
    minI = 86
    maxI = 230
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO

def normalizeGreen(intensity):
    iI = intensity
    minI = 90
    maxI = 225
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO

def normalizeBlue(intensity):
    iI = intensity
    minI = 100
    maxI = 210
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO

def histEqual():
    #https://levelup.gitconnected.com/introduction-to-histogram-equalization-for-digital-image-enhancement-420696db9e43
    orig_img = Image.open("/home/jerinpaul/Pictures/Unequalized_Hawkes_Bay_NZ.jpg")
    img = Image.open("/home/jerinpaul/Pictures/Unequalized_Hawkes_Bay_NZ.jpg")
    # convert to grayscale
    imgray = img.convert(mode='L')
    #convert to NumPy array
    img_array = np.asarray(imgray)
    """
    STEP 1: Normalized cumulative histogram
    """
    #flatten image array and calculate histogram via binning
    histogram_array = np.bincount(img_array.flatten(), minlength=256)
    #normalize
    num_pixels = np.sum(histogram_array)
    histogram_array = histogram_array/num_pixels
    #normalized cumulative histogram
    chistogram_array = np.cumsum(histogram_array)
    """
    STEP 2: Pixel mapping lookup table
    """
    transform_map = np.floor(255 * chistogram_array).astype(np.uint8)
    """
    STEP 3: Transformation
    """
    # flatten image array into 1D list
    img_list = list(img_array.flatten())
    # transform pixel values to equalize
    eq_img_list = [transform_map[p] for p in img_list]
    # reshape and write back into img_array
    eq_img_array = np.reshape(np.asarray(eq_img_list), img_array.shape)
    #convert NumPy array to pillow Image
    eq_img = Image.fromarray(eq_img_array, mode='L')
    orig_img.show()
    eq_img.show()


def correl():
    pass

def convo():
    pass

def smoothFilt():
    pass

def sharpFilt():
    pass

def grad():
    pass

def lap():
    pass

def main():
    flag = True
    while flag:
        print("\n 1. Negative Image\n 2. Contrast Stretching\n 3. Histogram Equalization\n 4. Correlation\n 5. Convolution\n 6. Smoothing Filters\n 7. Sharpening Filters\n 8. Gradient\n 9. Laplacian\n10. Exit\n")
        choice = int(input("Your Choice is: "))
        if choice == 1:
            negImg()
        elif choice == 2:
            contStretch()
        elif choice == 3:
            histEqual()
        elif choice == 4:
            correl()
        elif choice == 5:
            convo()
        elif choice == 6:
            smoothFilt()
        elif choice == 7:
            sharpFilt()
        elif choice == 8:
            grad()
        elif choice == 8:
            lap()
        else:
            flag = False

main()