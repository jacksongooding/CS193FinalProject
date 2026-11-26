#!/bin/bash
# devemopment test file, installs, adds items to the todo list and then runs the gui engine file

./install.sh

addtodo test4 12-12-2030
addtodo test4 12-12-2030
addtodo test4 12-12-2030
addtodo test1 12-12-2005
addtodo test1 12-12-2005
addtodo test1 12-12-2005
addtodo test3 12-12-2025
addtodo test3 12-12-2025
addtodo test3 12-12-2025
addtodo test2 12-12-2015
addtodo test2 12-12-2015
addtodo test2 12-12-2015

python3 ../../../.simple-todolist/GUI/GUI_app_engine.py
