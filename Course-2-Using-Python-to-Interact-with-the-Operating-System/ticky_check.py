#!/usr/bin/env python3

# import modules
import re
import csv
import operator

#initialize dictionaries
error_dict = {}
user_dict = {}

#open syslog file in read only format
f = open("syslog.txt", "r")

#parse through the file using regex to match ticky
for line in f:
  result = re.search(r"ticky: ([\w+]*):? ([\w' ]*)[ ].*[ ]?\((.*)\)$", line)
  #group 1=INFO/ERROR, group2=comment, group3=username

  if result.group(3) not in user_dict.keys():  #check to see if user is already in the dictionary
    user_dict[result.group(3)] = {}
    user_dict[result.group(3)]["INFO"] = 0  #initialize user info count
    user_dict[result.group(3)]["ERROR"] = 0  #initialize user error count

  if result.group(1) == "ERROR":
    #check to see if error type is in the dictionary and increment the count
    if result.group(2) not in error_dict.keys(): 
      error_dict[result.group(2)] = 0
      error_dict[result.group(2)] += 1
    else:
      error_dict[result.group(2)] += 1

    user_dict[result.group(3)]["ERROR"] += 1

  elif result.group(1) == "INFO":
    user_dict[result.group(3)]["INFO"] += 1

  else:
    print("SOMETHING IS WRONG")

f.close()

#sort both dicts
user_dict = sorted(user_dict.items())  #alphabetical order
error_dict = sorted(error_dict.items(), key = operator.itemgetter(1), reverse = True)  #sorts in descending order by the value

#store in user_statistics.csv
with open("user_statistics.csv", "w") as f:
  f.write("Username, INFO, ERROR\n")
  for line in user_dict:
    user, value = line
    f.write(str(user)+", "+str(value["INFO"])+", "+str(value["ERROR"])+"\n")

#store in error_message.csv
with open("error_message.csv", "w") as f:
  f.write("Error, Count\n")
  for line in error_dict:
    error, count = line
    f.write(str(error)+", "+str(count)+"\n")

#testing
print("USER DICTIONARY", user_dict)
print("ERROR DICTIONARY", error_dict)
