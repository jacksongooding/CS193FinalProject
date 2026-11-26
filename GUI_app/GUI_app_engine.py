#!/usr/bin/python3

# imports
import pygame as lib
from json import loads, dumps
from os import path

def init():
    global WINDOW, WINX, WINY, xItems, upButton, downButton, bottomOverlayRect, BACKGROUND_COLOR, elementOffset, buttonColors

    # initalize pygame and sets everything up (named "lib," short for "library," for ease of use)
    lib.init()
    WINDOW = lib.display.set_mode((390, 520))
    WINX = lib.display.get_window_size()[0]
    WINY = lib.display.get_window_size()[1] - 40
    BACKGROUND_COLOR = lib.Color("cadetblue2")
    elementOffset = 0
    lib.display.set_caption("Todo List")
    try: 
        windowIcon = lib.image.load("./windowIcon")
        lib.display.set_icon(windowIcon)
    except: pass
    
    # creates the x box items for removing items
    xItems = []
    x = WINX - 40
    y = 10
    lenXY = 30
    for i in range(5):
        xItems.append({'rect': lib.Rect(x, y, lenXY, lenXY), 'color': lib.Color("red"), 'textColor': lib.Color("white")})
        y += WINY / 5
    buttonColors = [lib.Color("forestgreen"), lib.Color("gainsboro")] # 0: active, 1: inactive
    bottomOverlayRect = lib.Rect(0, WINY , WINX, WINY + 40)
    upButton = {'rect': lib.Rect(WINX - lenXY * 2 - 5, WINY + 5, lenXY, lenXY), 'color': buttonColors[1], 'textColor': lib.Color("black"), 'text': ' ^'}
    downButton = {'rect': lib.Rect(WINX - lenXY, WINY + 5, lenXY, lenXY), 'color': buttonColors[0], 'textColor': lib.Color("black"), 'text': ' v'}

def loadData():
    # get json data if it exists
    global data, items, textItems, jsonFullFileName

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
                "isRemoveable": True
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
            "color": lib.Color("darkslategray1"),
            "isRemoveable": False
        })
        textItems.append({
                "text": 'Nothing To Do =)',
                "color": lib.Color("black"),
                "rect": lib.Rect(x + 5, y + leny / 2 - 10, lenx, leny) 
            })
    if elementOffset + 5 < len(items): downButton['color'] = buttonColors[0]
    else: downButton['color'] = buttonColors[1]


def drawXItems(i):
    if i + elementOffset < len(items) and items[i + elementOffset]['isRemoveable']: 
        lib.draw.rect(WINDOW, xItems[i]['color'], xItems[i]['rect'])
        WINDOW.blit(lib.font.Font(None, size=40).render(' x', True, xItems[i]['textColor']), xItems[i]['rect'])

# main program loop
def main():
    global elementOffset

    keyPressed = lib.key.get_pressed()

    WINDOW.fill(BACKGROUND_COLOR)

    if len(items) != 0:
        for i in range(len(items)):
            if i + elementOffset < len(items):
                elementYOffset = (WINY / 5) * elementOffset
                lib.draw.rect(WINDOW, items[i + elementOffset]['color'], items[i + elementOffset]['rect'].move(0, -elementYOffset))
        for i in range(len(textItems)): 
            if i + elementOffset < len(items): WINDOW.blit(
                lib.font.Font(None, size=40).render(
                    textItems[i + elementOffset]['text'], 
                    True,
                    textItems[i + elementOffset]['color']), 
                    textItems[i + elementOffset]['rect'].move(0, -elementYOffset)
                )

        if len(items) < 5:
            for i in range(len(items)): drawXItems(i)
        else:
            for i in range(5): drawXItems(i) 

    lib.draw.rect(WINDOW, BACKGROUND_COLOR, bottomOverlayRect)
    lib.draw.rect(WINDOW, upButton['color'], upButton['rect'])
    lib.draw.rect(WINDOW, downButton['color'], downButton['rect'])
    WINDOW.blit(lib.font.Font(None, size=40).render(upButton['text'], True, upButton['textColor']), upButton['rect'])
    WINDOW.blit(lib.font.Font(None, size=40).render(downButton['text'], True, downButton['textColor']), downButton['rect'])

    ##framerate, quit events, and keyup events
    lib.display.flip()
    framerate = lib.time.Clock().tick(24)
    if keyPressed[lib.K_ESCAPE]:
        lib.quit()
        quit()
    for event in lib.event.get():
        if event.type == lib.QUIT: 
            lib.quit()
            quit()
        elif event.type == lib.MOUSEBUTTONUP:
            for i in range(len(xItems)):
                if xItems[i]['rect'].collidepoint(lib.mouse.get_pos()) and i + elementOffset < len(items) and items[i]['isRemoveable']:
                    items.pop(i + elementOffset)
                    textItems.pop(i + elementOffset)
                    data.pop(i + elementOffset)
                    with open(jsonFullFileName, 'w') as f: f.write(dumps(data))
                    loadData()
            if upButton['rect'].collidepoint(lib.mouse.get_pos()) and elementOffset > 0: 
                elementOffset -= 5
                if elementOffset == 0: upButton['color'] = buttonColors[1]
                if elementOffset + 5 < len(items): downButton['color'] = buttonColors[0]
                else: downButton['color'] = buttonColors[1]
            elif downButton['rect'].collidepoint(lib.mouse.get_pos()) and elementOffset + 5 < len(items): 
                elementOffset += 5
                upButton['color'] = buttonColors[0]
                if elementOffset + 5 < len(items): downButton['color'] = buttonColors[0]
                else: downButton['color'] = buttonColors[1]



init()
loadData()
while True: main()