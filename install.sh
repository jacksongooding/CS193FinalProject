#!/bin/bash

# Installs files to their proper place
# Destrucivly installs (deletes program files if those files are already installed)
# This is intended behavior

addTodoFullFilename="/home/${USER}/.local/bin/addtodo"
CLIappEngineFullFilename="/home/${USER}/.simple-todolist/CLI/CLI_app_engine.py"
CLIdirPath="/home/${USER}/.simple-todolist/CLI"
GUIdirPath="/home/${USER}/.simple-todolist/GUI"
jsonPath="/home/${USER}/.config/kdetodolist"
GUIappEngineFullFilename="/home/${USER}/.simple-todolist/GUI/GUI_app_engine.py"
todoFullFilename="/home/${USER}/Desktop/Todo"

./uninstall.sh --silent

mkdir -p $CLIdirPath
mkdir -p $GUIdirPath
mkdir -p $jsonPath
cp ./CLI_app/addtodo.sh $addTodoFullFilename
cp ./CLI_app/CLI_app_engine.py $CLIappEngineFullFilename
cp ./GUI_app/GUI_app_engine.py $GUIappEngineFullFilename
cp ./GUI_app/todo.sh $todoFullFilename
echo "Program Installed!"