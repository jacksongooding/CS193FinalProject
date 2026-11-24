#!/bin/bash

# Points to the GUI engine file

GUIappEngineFullFilename="/home/${USER}/.simple-todolist/GUI/GUI_app_engine.py"

if [ -f $GUIappEngineFullFilename ]; then
    python3 $GUIappEngineFullFilename
else
    notify-send "Error: Engine file does not exist! To fix this problem try running \"install.sh.\""
fi