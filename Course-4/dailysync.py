#!/usr/bin/env Python3

from multiprocessing import Pool
import subprocess
import os

# Replace "<studentID>" with your own
src = "/home/<studentID>/data/prod/"
dest = "/home/<studentID>/data/prod_backup/"

def run(item):
    subprocess.call(["rsync", "-arq", src, dest])  #sync data from src to dest

folder = []

# Traverse the src directory and add the contents to the list
for path, dir, file in os.walk(src):
    folder.append(dir)

# Create a Pool class and execute the function on the contents of the list 
p = Pool(len(folder))
p.map(run, folder)
