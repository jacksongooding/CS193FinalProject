#!/bin/bash

# Fully deletes the program files

addTodoFullFilename="/home/${USER}/.local/bin/addtodo"
appDirPath="/home/${USER}/.simple-todolist"
jsonPath="/home/${USER}/.config/kdetodolist"
cronJobFullFilename="/home/${USER}/.config/autostart/todolist"
cronJobDesktopfileFullFilename="/home/${USER}/.config/autostart/todolist.desktop"
todoFullFilename="/home/${USER}/Desktop/Todo"
silent="--silent"

if [ -d $appDirPath ]; then
    rm -r "/home/${USER}/.simple-todolist"
fi
if [ -f $addTodoFullFilename ]; then 
    rm $addTodoFullFilename 
fi
if [ -f $todoFullFilename ]; then 
    rm $todoFullFilename 
fi
if [ -f $cronJobFullFilename ]; then 
    rm $cronJobFullFilename
fi
if [ -f $cronJobDesktopfileFullFilename ]; then 
    rm $cronJobDesktopfileFullFilename
fi
if [ -d $jsonPath ]; then
    rm -r $jsonPath
fi
if [[ $silent != $1 ]]; then
    echo "Program Uninstalled Successfully"
fi