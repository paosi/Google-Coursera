#!/bin/bash

# Create an empty file to hold all the filenames that need to be changed
> oldFiles.txt

# Find the entries that contain the name Jane using grep and return the field that contains the filename
files=$(grep " jane " ../data/list.txt | cut -d " " -f 3)

# Testing
# echo $files

for i in $files; do
	# Test if the file exists in the directory and if True, append the entry to oldFiles.txt
	if test -e /home/<username>$i; then echo $i >> oldFiles.txt; fi
done