#! /usr/bin/env python3

import os
import requests

# Point to the folder which contains the feedback txt files
source = "/data/feedback/"

def post_feedback():
    
    # Initialize feedback dict and set key values for feedback dict
    key_list = ["title", "name", "date", "feedback"]

    # Initialize dictionary that will be sent web service
    all_feedback = {}

    for file in os.listdir(source):
        #print(file)  # Testing
        feedback = {}
        
        # Assign each dict key a value from the corresponding line in the file
        with open(source + file, "r") as f:
            i = 0
            for line in f:
                feedback[key_list[i]] = line.strip()
                i += 1
                #print(feedback)

        # Add the contents of the dict as the value to the main dict
        all_feedback[file] = feedback

    #print(all_feedback)
    
    # Return a dictionary with the txt file as the key and the content of the txt file as the value
    return all_feedback
    
#post_feedback()

url = "http://<corpweb-external-IP>/feedback/feedback/"  # Make sure to append the "/" at the end of the URL!!!
upload = post_feedback()

# Submit POST request, print response text and status code
for key, value in upload.items():

    r = requests.post(url, data = value)

    if not r.ok:
        raise Exception("ERROR {x}".format(x = r.status_code))
    else:
        print("Successfully added {x} - Status code: {y}".format(x = key, y = r.status_code))
