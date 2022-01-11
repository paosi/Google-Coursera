# Course 4 - Troubleshooting and Debugging Techniques

# Week 2 Lab: 

Problem Statement:

You're an IT administrator for a media production company that uses Network-Attached Storage (NAS) to store all data generated daily (e.g., videos, photos). One of your daily tasks is to back up the data in the production NAS (mounted at /data/prod on the server) to the backup NAS (mounted at /data/prod_backup on the server). A former member of the team developed a Python script (full path /scripts/dailysync.py) that backs up data daily. But recently, there's been a lot of data generated and the script isn't catching up to the speed. As a result, the backup process now takes more than 20 hours to finish, which isn't efficient at all for a daily backup.

Requirements:
- Identify what limits the system performance: I/O, Network, CPU, or Memory
- Use rsync command instead of cp to transfer data
- Get system standard output and manipulate the output
- Find differences between threading and multiprocessing

Solution:

Create "dailysync.py file" and use multiprocessing and subprocess modules to sync data from the source directory to the backup directory. Define a run() method to perform the task. Traverse the source directory and add the sub-directories to a "folder[]" list. Create an object of the Pool class from the multiprocessing module with the length of "folder[]" as the parameter. Start each task within the pool object by calling the map instance method, and pass the run function and "folder[]" as the arguments.