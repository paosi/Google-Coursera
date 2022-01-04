#!/usr/bin/env python3

import os
from PIL import Image


def edit_images(source):

    # Creates the directory if it doesn't exist
    if not os.path.exists(destination):
        os.makedirs(destination)

    for img in os.listdir(source):

        try:
            new_img = Image.open(source + img)

        # Sets an exception for non-image files
        except IOError:
            print("File {x} is not an image file".format(x = img))
            continue
        
        else:
            # Size: Change image resolution from 3000x2000 to 600x400 pixel
            # Format: Change image format from .TIFF to .JPEG    
            # Convert to RGB mode (Cannot convert to JPEG unless this is done first)
            # Save as JPEG file in destination folder
            new_img.convert("RGB").resize((600, 400)).save(destination + img + ".jpg", "JPEG")
            print("Edited the image")


# source = "~/supplier-data/images/"
source = "/Users/paolosidera/Desktop/Coursera/Google_IT/PIL/images/"
destination = "/Users/paolosidera/Desktop/Coursera/Google_IT/final/img_edits/"

edit_images(source)