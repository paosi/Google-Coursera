#!/usr/bin/env python3

#import python modules
import sys
import re
import csv
import operator

#initialize dictionaries
count_errors = {}
count_per_user = {}

#parse through each entry in the syslog file

f = open("syslog.log", 'r')

for line in f:
	result = re.search(r"ticky: ([\w+]*):? ([\w' ]*) [\[[0-9#]*\]?]? ?\((.*)\)$", line)
        
#check if it matches INFO or ERROR format using regex and add matches to per_user and error dicts
  if result.group(2) not in count_errors.keys():
    count_errors[result.group(2)] = 0
  count_errors[result.group(2)] += 1
  if result.group(3) not in count_per_user.keys():
    count_per_user[result.group(3)] = {}
    count_per_user[result.group(3)]["INFO"] = 0
    count_per_user[result.group(3)]["ERROR"] = 0

  if result.group(1) == "INFO":
		count_per_user[result.group(3)]["INFO"] += 1
  elif result.group(1) == "ERROR":
    count_per_user[result.group(3)]["ERROR"] += 1


#sort both dicts
count_errors = sorted(count_errors.items(), key = operator.itemgetter(1), reverse = True)
count_per_user = sorted(count_per_user.items())



#store in error_message.csv and user_statistics.csv
f.close()
count_errors.insert(0, ('Error', 'Count'))

f = open(error_message, 'w')
for error in count_errors:
	a,b = error
  f.write(str(a)+','+str(b)+'\n')
f.close()

f = open(user_statistics, 'w')
f.write("Username,INFO,ERROR\n")
for stats in count_per_user:
	a, b = stats
  f.write(str(a)+','+str(b["INFO"])+','+str(b["ERROR"])+'\n')
f.close()


