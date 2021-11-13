from PIL import Image
import os

path = ""
resize_ratio = 0.5  # where 0.5 is half size, 2 is double size

def resize_aspect_fit():
    dirs = os.listdir()
    for item in dirs:
        if item == 'compress_image.py':
            continue
        if os.path.isfile(path+item):
            image = Image.open(path+item)
            file_path, extension = os.path.splitext(path+item)

            new_image_height = int(image.size[0] / (1/resize_ratio))
            new_image_length = int(image.size[1] / (1/resize_ratio))

            image = image.resize((new_image_height, new_image_length), Image.ANTIALIAS)
            image.save(file_path + "_small" + extension, 'JPEG', quality=90)


resize_aspect_fit()