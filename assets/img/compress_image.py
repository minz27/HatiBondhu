import os
import glob
import PIL
from PIL import Image

def compress_images():
	images = [file for file in os.listdir() if file.lower().endswith(('jpg', 'png', 'jpeg' ))]
	for image in images:
		if image == "hec.jpg":
			continue
		img = Image.open(image)
		img.save(image, optimize=True,quality=60)

if __name__ == '__main__':
	compress_images()

		