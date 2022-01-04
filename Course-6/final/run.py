#! /usr/bin/env python3

import os
import requests

# Set endpoint url for file upload
url = "https://httpbin.org/post"

# Set the keys for the post object
key_list = ["name", "weight", "description", "image_name"]

def fruit_upload(source):

    for file in os.listdir(source):
        
        # Iterate through the lines in the file and assign each to the corresponding key
        # Store results in a dict
        fruits = {}
        with open(source + file, "r") as f:
            i = 0
            for line in f:
                fruits[key_list[i]] = line.strip()
                i += 1
            fruits[key_list[3]] = file
            #print(fruits)
        
        # Post the result to the web server
        r = requests.post(url, data = fruits)

        # Checks if post was successful and returns status code
        if not r.ok:
            raise Exception("ERROR {x}".format(x = r.status_code))
        else:
            print("Successfully added {x} - Status code: {y}".format(x = file, y = r.status_code))


source = "/Users/paolosidera/Git/Google-Coursera/Course-6/final/supplier-data/descriptions/"
fruit_upload(source)
