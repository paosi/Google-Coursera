#!/usr/bin/env python3

import psutil
import shutil
import socket

def health_check():

    error_msg = ""

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
    if memory.available/(1024*1025) < 500:
        error_msg = "Error - Available memory is less than 500MB"

    #Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
    host = socket.gethostbyname("localhost")
    if host != "127.0.0.1":
        error_msg = "Error - localhost cannot be resolved to 127.0.0.1"

    return error_msg

status = health_check()

if status != "":
    print("NOT GOOD")
    sender = "automation@example.com"
    receiver = "{x}@example.com".format(x = "<USER>")
    subject = status
    body = "Please check your system and resolve the issue as soon as possible."