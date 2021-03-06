import struct
from PIL import Image, ImageOps
import numpy as np

fn = "/home/jerinpaul/Documents/ME/Sem 2/IP/sample_640×426.bmp"
bmp = open(fn, 'rb')
print(bmp)
print('Type:', bmp.read(2).decode())
print('Size: %s' % struct.unpack('I', bmp.read(4)))
print('Reserved 1: %s' % struct.unpack('H', bmp.read(2)))
print('Reserved 2: %s' % struct.unpack('H', bmp.read(2)))
print('Offset: %s' % struct.unpack('I', bmp.read(4)))

print('DIB Header Size: %s' % struct.unpack('I', bmp.read(4)))
width, height = struct.unpack('I', bmp.read(4))[0], struct.unpack('I', bmp.read(4))[0]
print('Width: ' + str(width))
print('Height: ' + str(height))
print('Colour Planes: %s' % struct.unpack('H', bmp.read(2)))
print('Bits per Pixel: %s' % struct.unpack('H', bmp.read(2)))
print('Compression Method: %s' % struct.unpack('I', bmp.read(4)))
print('Raw Image Size: %s' % struct.unpack('I', bmp.read(4)))
print('Horizontal Resolution: %s' % struct.unpack('I', bmp.read(4)))
print('Vertical Resolution: %s' % struct.unpack('I', bmp.read(4)))
print('Number of Colours: %s' % struct.unpack('I', bmp.read(4)))
print('Important Colours: %s' % struct.unpack('I', bmp.read(4)))

print('Red Colour: %s' % struct.unpack('I', bmp.read(4)))
print('Green Colour: %s' % struct.unpack('I', bmp.read(4)))
print('Blue Colour: %s' % struct.unpack('I', bmp.read(4)))
print('Alpha Channel Bitmask: %s' % struct.unpack('I', bmp.read(4)))
print('Color Space Type: %s' % struct.unpack('I', bmp.read(4)))
print('Color Space Endpoints: %s' % struct.unpack('I', bmp.read(4)))
print('Gamma for red channel: %s' % struct.unpack('I', bmp.read(4)))
print('Gamma for green channel: %s' % struct.unpack('I', bmp.read(4)))
print('Gamma for blue channel: %s' % struct.unpack('I', bmp.read(4)))
print('Intent: %s' % struct.unpack('I', bmp.read(4)))
print('ICC Profile Data: %s' % struct.unpack('I', bmp.read(4)))
print('ICC Profile Size: %s' % struct.unpack('I', bmp.read(4)))
print('Reserved: %s' % struct.unpack('I', bmp.read(4)))

def read_rows(path, w, h):
	image_file = open(path, "rb")
	image_file.seek(52)
	rows = []
	row = []
	pixel_index = 0
	RBand, GBand, BBand = [], [], []
	rchannel, gchannel, bchannel = [], [], []

	while True:
		if pixel_index == w:
			pixel_index = 0
			rows.insert(0, row)
			RBand.append(rchannel)
			GBand.append(gchannel)
			BBand.append(bchannel)
			#if len(row) != w * 3:
			#	print("Error!")
			row = []
			rchannel, gchannel, bchannel = [], [], []
		pixel_index += 1

		r_string = image_file.read(1)
		g_string = image_file.read(1)
		b_string = image_file.read(1)

		if len(r_string) == 0:
			if len(rows) != h:
				print("Warning!!! Read to the end of the file!")
			break

		if len(g_string) == 0:
			print("Warning!!! Got 0 length string for green. Breaking.")
			break

		if len(b_string) == 0:
			print("Warning!!! Got 0 length string for blue. Breaking.")
			break
		temp = []
		r = ord(r_string)
		g = ord(g_string)
		b = ord(b_string)

		temp.append(b)
		temp.append(g)
		temp.append(r)
		row.append(temp)
		rchannel.append(r)
		gchannel.append(g)
		bchannel.append(b)

	image_file.close()
	return RBand, GBand, BBand

imgR, imgG, imgB = read_rows(fn, width, height)
imgR, imgG, imgB = Image.fromarray(np.array(imgR[::-1], dtype=np.uint8)), Image.fromarray(np.array(imgG[::-1], dtype=np.uint8)), Image.fromarray(np.array(imgB[::-1], dtype=np.uint8))
img = Image.merge("RGB", (imgR, imgG, imgB))
img1 = ImageOps.grayscale(img)
img.show()
img1.show()
#sub_pixels = repack_sub_pixels(rows, width, height)
