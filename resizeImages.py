import os
from PIL import Image

def resize_images(input_folder, output_folder, width, height):
    """
    Resizes and crops all images in the input_folder to the specified width and height, and saves the resulting images
    to the output_folder.
    """
    for filename in os.listdir(input_folder):
        # Open the image file
        with Image.open(os.path.join(input_folder, filename)) as image:
            # Resize and crop the image
            resized_image = image.resize((width, height))
            left = (resized_image.width - width) / 2
            top = (resized_image.height - height) / 2
            right = (resized_image.width + width) / 2
            bottom = (resized_image.height + height) / 2
            cropped_image = resized_image.crop((left, top, right, bottom))
            # Save the resulting image to the output folder
            cropped_image.save(os.path.join(output_folder, filename))
            
# input_folder = './markedResizeBefore'
# output_folder = './markedResizeAfter'
input_folder = './originalResizeBefore'
output_folder = './originalResizeAfter'
width = 960
height = 720

resize_images(input_folder, output_folder, width, height)
