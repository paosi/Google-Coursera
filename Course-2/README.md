# Course 2 - Using Python to Interact with the Operating System

# Week 6 Lab: Editing Files Using Substrings
# changeJane.py, findJane.sh

Problem Statement:

In this lab, you'll change the username of your coworker Jane Doe from "jane" to "jdoe" in compliance with company's naming policy. The username change has already been done. However, some files that were named with Jane's previous username "jane" haven't been updated yet. To help with this, you'll write a bash script and a Python script that will take care of the necessary rename operations.

Requirements:
- Practice using the cat, grep, and cut commands for file operations
- Use > and >> commands to redirect I/O stream
- Replace a substring using Python
- Run bash commands in Python

Solution:

Create a bash script "findJane.sh" which will take the filenames from "list.txt" which contain the username "jane" and add them to a new file, "oldFiles.txt". But first, we must run a test to make sure the file in the "list.txt" file actually exists in the directory, so we add a test for that. The filenames that pass the test are addded to "oldFiles.txt".

Then, create a file "changeJane.py" which will take the file names in the source file, "oldFiles.txt" and convert them into the new format. When "changeJane.py" is executed, the converted filenames should be present in the directory.


# Week 7 Lab: Log Analysis Using Regular Expressions
# ticky_check.py

Problem Statement:

Imagine your company uses a server that runs a service called ticky, an internal ticketing system. The service logs events to syslog, both when it runs successfully and when it encounters errors.

The service's developers need your help getting some information from those logs so that they can better understand how their software is used and how to improve it. So, for this lab, you'll write some automation scripts that will process the system log and generate reports based on the information extracted from the log files.

Requirements:

- Use regex to parse a log file
- Append and modify values in a dictionary
- Write to a file in CSV format
- Move files to the appropriate directory for use with the CSV->HTML converter

Solution:

Project requires parsing a "syslog" source file using regex and creating 2 separate dictionaries in "ticky_check.py" file. The information in these dictionaries will then be written to two .csv files, "user_statistics.csv" and "error_message.csv", which will then be converted to html files. These html files can be viewed on the browser with the following desired output:


<img width="327" alt="error_message_html" src="https://user-images.githubusercontent.com/7923788/146034419-0bce31c8-ee5b-4d39-85df-2e1eb476e628.png">
<img width="328" alt="user_statistics_html" src="https://user-images.githubusercontent.com/7923788/146034423-aa6e389d-0e47-481a-b740-bccd584fd28c.png">
