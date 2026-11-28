#!/bin/bash

cronJobFullFilename="/home/${USER}/.config/autostart/todolist"
cp ./Autostart/autostart.sh $cronJobFullFilename
echo "success!"
echo "To make the script start: go to settings > System > Autostart, click on Add New then Login Script..."
echo "Then type .config/autostart/todolist and hit enter"
echo "now Todo list will open upon login"