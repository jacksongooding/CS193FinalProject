#!/bin/bash
# originally the devemopment test file, installs, adds items to the todo list and then runs the gui engine file

./install.sh

addtodo test 11-25-2026
addtodo test 11-26-2026
addtodo test 11-27-2026
addtodo test 11-28-2026
addtodo test 11-29-2026
addtodo test 11-30-2026
addtodo test 12-1-2026
addtodo test 12-2-2026
addtodo test 12-3-2026
addtodo test 12-5-2026
addtodo test 12-8-2026
addtodo test 1-3-2027

python3 ../../../.simple-todolist/GUI/GUI_app_engine.py
