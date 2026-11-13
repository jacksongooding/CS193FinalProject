#!/bin/bash

# Fully deletes the program files

addTodoFullFilename="/home/${USER}/.local/bin/addtodo"
CLIappEngineFullFilename="/home/${USER}/.simple-todolist/CLI/CLI_app_engine.py"
jsonPath="/home/${USER}/.config/kdetodolist"
CLIdirPath="/home/${USER}/.simple-todolist/CLI"
silent="--silent"

if [ -d $CLIdirPath ]; then
    rm -r "/home/${USER}/.simple-todolist"
fi
if [ -f $addTodoFullFilename ]; then 
    rm $addTodoFullFilename 
fi
if [ -f $CLIappEngineFullFilename ]; then
    rm $CLIappEngineFullFilename
fi
if [ -d $jsonPath ]; then
    rm -r $jsonPath
fi
if [[ $silent != $1 ]]; then
    echo "Program Uninstalled Successfully"
fi