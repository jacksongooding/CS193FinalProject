# KDE TODO List

A custom todo list for KDE that I can easily update and acess without having to rely on documents/calenders.

## The Problem

I am inconsistent with updating calendars with assignments and my todo list document does not run on startup leading me to be somewhat disorganized. 

## How It Works

This project is a small applicaton which compiles a taskes specified in a .json file and displays them as elements which 
can be removed when done. A small terminal program is used to add elements to a json file which the graphical program uses
to build a list of tasks to do. These tasks are color coded starting green when you have several days and slowly getting redder until their late. This program leverages Pygame's Rects and fonts to create a UI.

Note: This program is designed to work only with the Linux file structure. It will not run on windows.


## Tech Stack

- **Language:** Python, Bash
- **Libraries:** Pygame, json, os, datetime
- **External tools:** json

## Setup

```bash
git clone https://github.com/jacksongooding/CS193FinalProject
cd CS193FinalProject
./install.sh
```

Additionally you can run:

```bash
git clone https://github.com/jacksongooding/CS193FinalProject
cd CS193FinalProject
./demo_install.sh
```

This will auto install, add items, and run the program

For KDE Plasma users there is an autostart script that you can install using the commands below.
(this is a seperate file to give users the choice if they want it without pushing them to do it)

```bash
git clone https://github.com/jacksongooding/CS193FinalProject
cd CS193FinalProject
./install_autostart.sh
```
You will have to manually make the script start, however.
To do this go to settings > System > Autostart, click on Add New then Login Script... Then type .config/autostart/todolist and hit enter

## Uninstall
To uninstall this program simply run the commands below:

```bash
cd CS193FinalProject
./uninstall.sh
```
If you deleted the cloned repo, no worries, simply clone the repo again and run the commands above.
uninstall.sh also removes the autostart files as well.

## Usage
To add elements to the list run addtodo \[name\], \[mm/dd/yyyy\]
Note: to put spaces in the name use a "-" seperator
To open the GUI application click on the "todo" script added to your desktop
To remove an element just press the "x"
To scroll over elements click the "v" or "^" buttons (clicking scrolls 5 elements at a time)


## Roadmap for MVP

- [x] Add Terminal Based task adding of tasks
- [x] Add a graphical Display of tasks I have to do
- [x] Add graphical controls and make the interface more dynamic
- [x] Add dynamic color changer for task importance/overdue tasks + instant update after CLI addition

## Additional Features (Important, Not Urgent)

- [x] Make the program autostart on login
- [ ] Add Sprites to make the program more visually asthetic
- [ ] Add GUI based task adding

## Author

Jackson, https://github.com/jacksongooding
