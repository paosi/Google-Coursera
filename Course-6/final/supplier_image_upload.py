#! /usr/bin/env python3

import requests
import os

url  = "[linux-instance-IP-Address]/upload/"

def post_image(source):

    # Iterate over each file in the source directory
    for img in os.listdir(source):

        # Sends a post request to the webserver only if the file is an image
        with open(source + img, "rb") as opened:
            if ".jpeg" in img:
                r = requests.post(url, files = {"file": opened})
                if not r.ok:
                    raise Exception("ERROR {x}".format(x = r.status_code))
                else:
                    print("Successfully added {x} - Status code: {y}".format(x = opened, y = r.status_code))
            else:
                print("File {x} not a valid JPEG file".format(x = img ))
  

source = "supplier-data/images/"
post_image(source)