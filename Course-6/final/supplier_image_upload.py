#!/usr/bin/env python3

import requests
import os

#url  = "[linux-instance-IP-Address]/upload/"
url = "https://httpbin.org/post"
#source = "/supplier-data-images/"
source = "/Users/paolosidera/Git/Google-Coursera/Course-6/final/img_edits/"

for img in os.listdir(source):

    with open(source + img, "rb") as opened:
        if ".jpg" in img:
            r = requests.post(url, files = {"file": opened})
            if not r.ok:
                raise Exception("ERROR {x}".format(x = r.status_code))
            else:
                print("Successfully added {x} - Status code: {y}".format(x = opened, y = r.status_code))
        else:
            print("File {x} not a valid JPEG file".format(x = img ))
  