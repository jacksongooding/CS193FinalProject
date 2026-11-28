#!/bin/bash
# executes the app on startup

GUIappEngineFullFilename="/home/${USER}/.simple-todolist/GUI/GUI_app_engine.py"

if [ -f $GUIappEngineFullFilename ]; then 
    python3 $GUIappEngineFullFilename
fi
