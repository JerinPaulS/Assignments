#from statistics import correlation
from audioop import mul
from turtle import clear
from unittest import result
from PIL import Image, ImageOps
from PIL import ImageFilter
import matplotlib.pyplot as plt
import numpy as np
import cv2
from yaml import MappingNode

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

def lowPass():
    img = cv2.imread('/home/jerinpaul/Pictures/stones.jpeg', 0)
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    #magnitude_spectrum = 20 * np.log((cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))+1)

    rows, cols = img.shape
    center_row, center_col = rows // 2, cols // 2
    radius = 120
    center = [center_row, center_col]
    mask = np.ones((rows, cols, 2), np.uint8)
    x, y = np.ogrid[:rows, : cols]
    mask_area = ((x - center[0] ** 2) + (y - center[1]) ** 2) <= radius ** 2
    mask[mask_area] = 0

    fshift = dft_shift * mask
    #fshift_mask_mag = 20 * 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]) + 1)
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    fig = plt.figure(figsize=(15,15))
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.imshow(img, cmap='gray')
    ax1.title.set_text("Original Image")
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.imshow(img_back, cmap='gray')
    ax2.title.set_text("Processed Image")
    plt.show()

def highPass():
    img = cv2.imread('/home/jerinpaul/Pictures/stones.jpeg', 0)
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)
    mask = np.zeros((rows, cols, 2), np.uint8)
    r = 100
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
    mask[mask_area] = 1
    
    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)
    mask = np.zeros((rows, cols, 2), np.uint8)
    r_out = 80
    r_in = 10
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = np.logical_and(((x - center[0]) ** 2 + (y - center[1]) ** 2 >= r_in ** 2),
                            ((x - center[0]) ** 2 + (y - center[1]) ** 2 <= r_out ** 2))
    mask[mask_area] = 1

    fshift = dft_shift * mask
    #fshift_mask_mag = 20 * 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]) + 1)
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    fig = plt.figure(figsize=(15,15))
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.imshow(img, cmap='gray')
    ax1.title.set_text("Original Image")
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.imshow(img_back, cmap='gray')
    ax2.title.set_text("Processed Image")
    plt.show()

def gaussianFilter():
    pass

def laplacianFilter():
    pass

def main():
    flag = True
    while flag:
        #print("\n 1. Negative Image\n 2. Contrast Stretching\n 3. Histogram Equalization\n 4. Correlation\n 5. Convolution\n 6. Smoothing Filters\n 7. Sharpening Filters\n 8. Gradient\n 9. Laplacian\n10. Exit\n")
        print("\n 1. Negative Image\n 2. Contrast Stretching\n 3. Histogram Equalization\n 4. Correlation\n 5. Low Pass Filter\n 6. High Pass Filter\n 7. Gaussian Filter\n 8. Laplacian Filter\n 9. Exit\n")
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
            lowPass()
        elif choice == 6:
            highPass()
        elif choice == 7:
            gaussianFilter()
        elif choice == 8:
            laplacianFilter()
        else:
            flag = False

main()