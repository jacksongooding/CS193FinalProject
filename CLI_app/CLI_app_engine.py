#!/usr/bin/python3

from json import dumps, loads
from sys import argv as args
from os import path
import datetime

# This is python logic for the CLI program
# This CLI program can write to the JSON file
# It can also read from the JSON file as well

# args should follow the following format
# 0: title, 1: due date, 2: maybe add more params later

# file read section #
# This is because the file needs to add elements to the list
global argDicts

jsonPath = path.dirname(path.abspath(__file__)) + "/../../.config/kdetodolist" 
jsonFullFileName = jsonPath + "/data.json"

try:
    with open(jsonFullFileName) as f: argDicts = loads(f.read())
except FileNotFoundError: argDicts = []

# args section #
if len(args) < 2: raise ValueError("Must provide at least two arguments: name and then due date")

global newItemDate

try:
    newItemDate = args[2].replace("-", "/")
    newItemDate = newItemDate.split("/")
    args[2] = datetime.datetime(int(newItemDate[2]), int(newItemDate[0]), int(newItemDate[1]))
except: 
    print("Date format is incorrect, it should be mm/dd/yyyy or mm-dd-yyyy")
    exit()

# converts the date into a big number to compare and insert in order
# that way I can check a single int and not year then month then day over many if loops
didAddItem = False
newItemDateNumber = int(newItemDate[2]) * 10000 + int(newItemDate[0]) * 100 + int(newItemDate[1])
args[1] = args[1].replace('-', ' ')

for i in range(len(argDicts)):
    date = argDicts[i]["date"].replace(" 00:00:00", "").replace('-', '/').split('/')
    currItemDateNumber = int(date[0]) * 10000 + int(date[1]) * 100 + int(date[2])

    if newItemDateNumber < currItemDateNumber:
        argDicts.insert(i, {"name": args[1], "date": str(args[2])})
        didAddItem = True
        break

if not didAddItem: argDicts.append({"name": args[1], "date": str(args[2])})

# file write section #
global openedFile

try: openedFile = open(jsonFullFileName, 'x')
except FileExistsError: openedFile = open(jsonFullFileName, 'w')

openedFile.write(dumps(argDicts))
openedFile.close()