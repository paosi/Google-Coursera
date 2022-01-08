#!/usr/bin/env python3

import os
import reports
import emails
from datetime import date

# Create a list that will store a dictionary key, value pair ("name", "weight")
def body_text(source):

    key_list = ["name", "weight"]
    p_list = []

    for file in os.listdir(source):
        s = []
        p = {}
        with open(source + file, "r") as f:
            i = 0
            for line in f:
                if i < 2:
                    p[key_list[i]] = line.strip() + "<br />"
                    i += 1             
                else:
                    continue
            for key, value in p.items():
                s.append("{x}: {y}".format(x = key, y = value))

            # Add line breaks after list pairs, for pdf formatting    
            p_list.append(s)
            p_list.append("<br />")

    # Turn list into a string
    paragraph = ""
    for item in p_list:
        paragraph += "".join(item)
    print(paragraph)
    return paragraph



source = "supplier-data/descriptions/"

# Define parametes for generate_report()
attachment = "/tmp/processed.pdf"
title = "Processed Update on {x}".format(x = date.today().strftime("%B %d, %Y"))
paragraph = body_text(source)

# Format email
sender = "automation@example.com"
receiver = "{x}@example".format(x = "user")
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

if __name__ == "__main__":

    reports.generate_report(attachment, title, paragraph)
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
