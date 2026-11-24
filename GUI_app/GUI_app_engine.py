#!/usr/bin/python3

# imports
import pygame as lib
from json import loads
from os import path

def init():
    global WINDOW, WINX, WINY

    # initalize pygame and sets everything up (named "lib" for ease of use)
    lib.init()
    WINDOW = lib.display.set_mode((390, 480))
    WINX = lib.display.get_window_size()[0]
    WINY = lib.display.get_window_size()[1]
    lib.display.set_caption("Todo List")
    try: 
        windowIcon = lib.image.load("./windowIcon")
        lib.display.set_icon(windowIcon)
    except: pass

def loadData():
    # get json data if it exists
    global data, items, textItems

    # the working directory in python is the directory of the terminal, not the script file
    # this gets the actual path to the script
    jsonPath = path.dirname(path.abspath(__file__)) + "/../../.config/kdetodolist"
    jsonFullFileName = jsonPath + "/data.json" 

    if (path.exists(jsonPath)):
        with open(jsonFullFileName) as f: data = loads(f.read())
    else: data = []
    
    items = []
    textItems = []
    block = WINY / 5
    x = 10
    y = block * 0.1
    lenx = WINX - x * 2 
    leny = block - y
    
    if len(data) != 0:
        for i in range(len(data)):
            items.append({
                "rect": lib.Rect(x, y, lenx, leny),
                "color": lib.Color("darkslategray1"),
            })

            textItems.append({
                "text": data[i]["name"] + " " + data[i]["date"],
                "color": lib.Color("black"),
                "rect": lib.Rect(x + 5, y + leny / 2 - 10, lenx, leny) 
            })

            y += block
    else:
        items.append({
            "rect": lib.Rect(x, y, lenx, leny),
            "color": lib.Color("cadetblue2"),
            "text": "Nothing todo =)",
        })

# main program loop
def main():
    keyPressed = lib.key.get_pressed()

    WINDOW.fill(lib.Color("cadetblue2"))

    if len(items) != 0:
        for item in items: lib.draw.rect(WINDOW, item['color'], item['rect'])
        for textItem in textItems: WINDOW.blit(lib.font.Font(None, size=40).render(textItem['text'], True, textItem['color']), textItem['rect'])
    
    ##framerate, quit events, and keyup events
    lib.display.flip()
    framerate = lib.time.Clock().tick(240)
    if keyPressed[lib.K_ESCAPE]:
        lib.quit()
        quit()
    for event in lib.event.get():
        if event.type == lib.QUIT: 
            lib.quit()
            quit()

init()
loadData()
while True: main()