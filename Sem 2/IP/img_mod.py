#from statistics import correlation
from audioop import mul
from turtle import clear
from unittest import result
from PIL import Image, ImageOps
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
    original = Image.open("/home/jerinpaul/Pictures/download.jpeg")
    original = ImageOps.grayscale(original)
    orig = np.array(original)
    img = []
    width, height = original.size
    for row in range(height):
        temp = []
        for col in range(width):
            temp.append(0)
        img.append(temp)

    for row in range(height - 2):
        for col in range(width - 2):
            temp = []
            temp.append(orig[row][col:col + 3])
            temp.append(orig[row + 1][col:col + 3])
            temp.append(orig[row + 2][col:col + 3])
            res = matmul(temp, [[1, 2, 3], [3, 2, 1], [2, 3, 4]])
            print(row, col)
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    img[i][j] = res[i - row][j - col]

    img = np.array(img)
    img = Image.fromarray(img.astype('uint8'))
    original.show()
    img.show()

def matmul(A, B):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def convo():
    pass

def smoothFilt():
    pass

def sharpFilt():
    original = Image.open("/home/jerinpaul/Pictures/download.jpeg")
    imageObject = Image.open("/home/jerinpaul/Pictures/download.jpeg")
    img = np.array(imageObject)
    imgR, imgG, imgB = [], [], []
    bandR, bandG, bandB = [], [], []
    width, height = original.size
    for row in range(height):
        temp = []
        temp1 = []
        temp2 = []
        temp3 = []
        for col in range(width):
            temp.append(0)
            temp1.append(img[row][col][0])
            temp2.append(img[row][col][1])
            temp3.append(img[row][col][2])
        imgR.append(temp)
        imgG.append(temp)
        imgB.append(temp)
        bandR.append(temp1)
        bandG.append(temp2)
        bandB.append(temp3)

    for row in range(height - 2):
        for col in range(width - 2):
            temp1 = []
            temp1.append(bandR[row][col:col + 3])
            temp1.append(bandR[row + 1][col:col + 3])
            temp1.append(bandR[row + 2][col:col + 3])
            temp2 = []
            temp2.append(bandG[row][col:col + 3])
            temp2.append(bandG[row + 1][col:col + 3])
            temp2.append(bandG[row + 2][col:col + 3])
            temp3 = []
            temp3.append(bandB[row][col:col + 3])
            temp3.append(bandB[row + 1][col:col + 3])
            temp3.append(bandB[row + 2][col:col + 3])
            res1 = matmul(temp1, [[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            res2 = matmul(temp2, [[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            res3 = matmul(temp3, [[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            print(row, col)
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    imgR[i][j] = res1[i - row][j - col]
                    imgG[i][j] = res2[i - row][j - col]
                    imgB[i][j] = res3[i - row][j - col]
    imgR, imgG, imgB = Image.fromarray(np.array(imgR, dtype=np.uint8)), Image.fromarray(np.array(imgG, dtype=np.uint8)), Image.fromarray(np.array(imgB, dtype=np.uint8))
    #imgR, imgG, imgB = ImageOps.invert(imgR), ImageOps.invert(imgG), ImageOps.invert(imgB)
    result = Image.merge("RGB", (imgR, imgG, imgB))
    original.show()
    result.show()

def low_grad():
    pass

def low_lap():
    pass

def high_grad():
    pass

def high_lap():
    pass

def main():
    flag = True
    while flag:
        #print("\n 1. Negative Image\n 2. Contrast Stretching\n 3. Histogram Equalization\n 4. Correlation\n 5. Convolution\n 6. Smoothing Filters\n 7. Sharpening Filters\n 8. Gradient\n 9. Laplacian\n10. Exit\n")
        print("\n 1. Negative Image\n 2. Contrast Stretching\n 3. Histogram Equalization\n 4. Correlation\n 5. Low - Gradient\n 6. Low - Laplacian\n 7. High - Gradient\n 8. High - Laplacian\n 9. Exit\n")
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
            low_grad()
        elif choice == 6:
            low_lap()
        elif choice == 7:
            high_grad()
        elif choice == 8:
            high_lap()
        #elif choice == 9:
        #    lap()
        else:
            flag = False

main()