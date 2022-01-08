#!/usr/bin/env python3

import psutil
import shutil
import socket
import emails

def health_check():

    #Report an error if CPU usage is over 80%
    amount_used = psutil.cpu_percent(1)
    if amount_used > 80:
        error_msg = "Error - CPU usage is over 80%"

    #Report an error if available disk space is lower than 20%
    used = shutil.disk_usage("/")
    amount_free = used.free * 100 / used.total
    if amount_free < 20:
        error_msg = "Error Available disk space is less than 20%"

    #Report an error if available memory is less than 500MB
    memory = psutil.virtual_memory()
    if memory.available/(1024*1024) < 500:
        error_msg = "Error - Available memory is less than 500MB"

    #Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
    host = socket.gethostbyname("localhost")
    if host != "127.0.0.1":
        error_msg = "Error - localhost cannot be resolved to 127.0.0.1"

    return error_msg


if __name__ == "__main__":

    try:
        status = health_check()  # Returns error_msg if one is present
        print(status)
        
        # Format email
        sender = "automation@example.com"
        receiver = "<USER>@example.com")
        subject = status
        body = "Please check your system and resolve the issue as soon as possible."

        # Generate error report and send email
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send_email(message)
        
    except UnboundLocalError:  # If no error_msg is present, pass the test
        print("System is healthy")

