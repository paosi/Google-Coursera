#!/usr/bin/env python3

import os
from PIL import Image


def edit_images(source):

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
            new_img.convert("RGB").resize((600, 400)).save(source + img.replace(".tiff", ".jpeg"), "JPEG")
            print("Edited the image")


source = "supplier-data/images/"
edit_images(source)