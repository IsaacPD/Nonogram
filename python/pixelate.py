from PIL import Image
from tkinter.filedialog import askopenfilename
import cv2
import os
#open a user selected image

def blackwhite(filename):
	im_gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
	(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	cv2.imwrite('bw_image.png', im_bw)
	return os.path.abspath("bw_image.png")
def cropping(source):
	height = source.size[1]
	width = source.size[0]
	rgb = source.convert('RGB')
	pixelList = []
	for i in range (height):
		for j in range (width):
			x, y, z = rgb.getpixel((j, i))
			if x == 0 and y == 0 and z == 0:
				pixelList.append(i)
				break	#get the top-most black pixel's y coor
		else:
			continue
		break

	for i in range (width):
		for j in range (height):
			x, y, z = rgb.getpixel((i, j))
			if x == 0 and y == 0 and z == 0:
				pixelList.append(i)
				break	#get the left most black pixel's x coor
		else:
			continue
		break

	for i in range (width-1, -1, -1):
		for j in range (height-1, -1, -1):
			x, y, z = rgb.getpixel((i, j))
			if x == 0 and y == 0 and z == 0:
				pixelList.append(i)
				break	#get the right most black pixel's x coor
		else:
			continue
		break

	for i in range (height-1, -1, -1):
		for j in range (width-1, -1, -1):
			x, y, z = rgb.getpixel((j,i))
			if x == 0 and y == 0 and z == 0:
				pixelList.append(i)
				break	#get the bottom most black pixel's y coor
		else:
			continue
		break
	return source.crop((pixelList[1], pixelList[0], pixelList[2], pixelList[3]))
	
def pixelate(input_file_path, width, height):
    image = Image.open(input_file_path)
    
    image = image.resize(
        (width * 2, height * 2),
        Image.NEAREST
    )
    image = cropping(image)
    image = image.resize(
        (width, height),
        Image.NEAREST
    )
    image = image.convert('RGB')
    return image

def pixelize(filename, width = 30, height = 30):
	return pixelate(blackwhite(filename), width, height)

if __name__ == '__main__':
	pixelize(askopenfilename()).save("pixelated.png")