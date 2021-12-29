#!/usr/bin/env python3

import sys
import subprocess

# Open the oldFiles.txt file in read only format and assign it to a variable
f = open(sys.argv[1], "r")

for line in f.readlines():  # Read through each line in the file 
  old_name = line.strip()
  new_name = old_name.replace("jane", "jdoe")
  subprocess.run(["mv", ".."+old_name, ".."+new_name])  # Updates file name

# Testing
# print(old_name, new_name)

f.close()