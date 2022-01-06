#!/usr/bin/env python3

import os
from datetime import date

import reports
import emails

key_list = ["name", "weight"]
p_list = []

# RETURN "paragraph" parameter
def body_text():

    for file in os.listdir(source):
        p = {}
        with open(source + file, "r") as f:
            i = 0
            for line in f:
                s = []
                if i < 2:
                    p[key_list[i]] = line.strip() + "</br>"
                    i += 1             
                else:
                    continue
            for key, value in p.items():
                s.append("{x}: {y}".format(x = key, y = value))
                
            p_list.append(s)
            p_list.append("</br>")

    paragraph = ""
    for item in p_list:
        paragraph += "".join(item)

    return paragraph


source = "/Users/paolosidera/Git/Google-Coursera/Course-6/final/supplier-data/descriptions/"
attachment = "/tmp/processed.pdf"
title = "Processed Update on {x}".format(x = date.today().strftime("%B %d, %Y"))
paragraph = body_text()
sender = "automation@example.com"
receiver = "{x}@example.com".format(x = os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

if __name__ == "__main__":

    reports.generate_report(attachment, title, paragraph)
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
