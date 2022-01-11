#!/usr/bin/env python3

import os
from PIL import Image

source = "/home/<student-id>/images/"

# Create a new directory for the edited images
destination = "/home/<student-id>/opt/icons/"

if not os.path.exists(destination):
   os.makedirs(destination)

# Iterate through the files in the source
for infile in os.listdir(source):

    try:
        im = Image.open(source + infile)

    # Sets an exception for non-image files
    except IOError:
        continue
    
    else:

        # Rotate the image counter-clockwise 270 degrees
        # Resize to 128 x 128
        # Convert to RGB mode (Cannot convert to JPEG unless this is done first)
        # Save as JPEG file in destination folder
        im.rotate(270).resize((128, 128)).convert("RGB").save(destination + infile, "JPEG")

