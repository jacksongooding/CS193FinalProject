#!/bin/bash

# Installs files to their proper place
# Destrucivly installs (deletes program files if those files are already installed)
# This is intended behavior

addTodoFullFilename="/home/${USER}/.local/bin/addtodo"
CLIappEngineFullFilename="/home/${USER}/.simple-todolist/CLI/CLI_app_engine.py"
CLIdirPath="/home/${USER}/.simple-todolist/CLI"
jsonPath="/home/${USER}/.config/kdetodolist"

./uninstall.sh --silent

mkdir -p $CLIdirPath
cp ./CLI_app/addtodo.sh $addTodoFullFilename
cp ./CLI_app/CLI_app_engine.py $CLIappEngineFullFilename
mkdir -p $jsonPath

echo "Program Installed!"