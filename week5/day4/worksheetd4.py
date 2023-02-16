import numpy as req
import translator as tr
import request as req
import datetime as dt

dt.datetime.now()



with open("week5/day4/words.txt", "w") as f:
    for i in range(100):
        f.write(str(i) + " word \n")

# Path: week5/day4/worksheetd4.py

for line in open("week5/day4/words.txt", "r"):
    print(line)


# Read the file line by line
# Read only the 5th line of the file
# Read only the 5th first characters of the file
# Read all the file and return it as a list of strings. Then split each word
# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# Append your first name at the end of the file
# Append "SkyWalker" next to each first name "Luke"

with open("week5/day4/nameslist.txt", "r") as f:
    print(f.readline)
with open("week5/day4/nameslist.txt", "r") as f:
    print(f.readlines())

with open("week5/day4/nameslist.txt", "r") as f:
    # read 5th line of the file namelist
    f.readlines()[5]
with open("week5/day4/nameslist.txt", "r") as f:
    # read 5th first characters of the file namelist
    f.read(5)
with open("week5/day4/nameslist.txt", "r") as f:
    print(f.read().split())
with open("week5/day4/nameslist.txt", "r") as f:
    print(f.read().count("Darth"))
    print(f.read().count("Luke"))
    print(f.read().count("Lea"))
with open("week5/day4/nameslist.txt", "r") as f:
    f.write("Sebastien")

with open("week5/day4/nameslist.txt", "r") as f:
    f.read().replace("Luke", "Luke Skywalker")

f.close()
