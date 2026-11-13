#!/bin/bash

# This file basically makes sure the system config is set up correctly before executing the file.

actualPath=$(dirname "$(realpath $0)")
devPath="/home/${USER}/de/tools/finalProj/CLI_app"
expectedPath="/home/${USER}/.local/bin"
expectedFullFilename="/home/${USER}/.local/bin/addtodo"
enginePath="/home/${USER}/.simple-todolist/CLI/CLI_app_engine.py"
jsonPath="/home/${USER}/.config/kdetodolist"

if [ $actualPath == $expectedPath ]; then
    if [ ! -d $jsonPath ]; then
        mkdir $jsonPath
    fi

    if [ ! -f $enginePath ]; then
        echo "Error: engine file does not exist!"
        echo "To fix this problem try running \"install.sh.\""
    else 
        python3 $enginePath $@
    fi
elif [ $actualPath == $devPath ]; then
    echo "You are currently in the dev enviroment context."
    python3 ./CLI_app_engine.py $@
else
    invalidIn=1
    while [ $invalidIn -eq 1 ]; do
        read -p "This file should be in ~/.local/bin, do you wish to copy it over [Y/n]: " in
        
        if [ ${in,,} = "y" ]; then  
            if [ -f $expectedFullFilename ]; then 
                echo "This file is already installed, run \"addtodo\" (without ./) in your terminal."
                echo "If you want to replace that file with this one, delete it and run this file again."
                invalidIn=0
            else
                mv $(realpath $0) $expectedFullFilename
                echo "Success!"
                echo "To execute this program: run \"addtodo\" (without ./) in your terminal."
                invalidIn=0
            fi
        elif [ ${in,,} = "n" ]; then
            echo "Unable to execute script; please move this file to ~/.local/bin"
            invalidIn=0
        else
            echo "Invalid input"
        fi
    done
fi