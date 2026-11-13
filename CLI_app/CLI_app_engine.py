from json import loads as read
from json import dumps as write
from sys import argv as args
import datetime

# This is python logic for the CLI program
# This CLI program can write to the JSON file
# It can also read from the JSON file as well

# args should follow the following format
# 0: title, 1: due date, 2: maybe add more params later

# args section #
if len(args) < 2: raise ValueError("Must provide at least two arguments: name and then due date")

try:
    localVar = args[2].split("/")
    args[2] = datetime.datetime(int(localVar[2]), int(localVar[0]), int(localVar[1]))
except: 
    print("Date format is incorrect, it should be mm/dd/yyyy")
    exit()

argDict = {"name": args[1], "date": str(args[2])}

# file section #
global openedFile
try: openedFile = open("../../../.config/kdetodolist/data.json", 'x')
except FileExistsError: pass

openedFile.write(write(argDict))