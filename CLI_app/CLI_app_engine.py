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
# maybe add color later?

localVar = ""

try:
    localVar = args[2].replace("-", "/")
    localVar = localVar.split("/")
    args[2] = datetime.datetime(int(localVar[2]), int(localVar[0]), int(localVar[1]))
except: 
    print("Date format is incorrect, it should be mm/dd/yyyy or mm-dd-yyyy")
    exit()

didAddItem = False
for i in range(len(argDicts)):
    date = argDicts[i]["date"].replace(" 00:00:00", "").replace('-', '/').split('/')

    # fix this logic later
    if int(localVar[0]) <= int(date[0]) and int(localVar[1]) <= int(date[1]) and int(localVar[2]) <= int(date[2]):
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