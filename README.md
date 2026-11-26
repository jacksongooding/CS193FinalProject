# KDE TODO List

A custom todo list for KDE that I can easily update and acess without having to rely on documents/calenders.

## The Problem

I am inconsistent with updating calendars with assignments and my todo list document does not run on startup leading me to be somewhat disorganized. 

## How It Works

This project is a small applicaton which compiles a taskes specified in a .json file and displays them as elements which 
can be removed when done. A small terminal program is used to add elements to a json file which the graphical program uses
to build a list of tasks to do. This program leverages Pygame's Rects and fonts to create a UI.

Note: This program is designed to work only with the Linux file structure. It will not run on windows.


## Tech Stack

- **Language:** Python, Bash
- **Libraries:** Pygame, python json library
- **External tools:** N/a

## Setup

```bash
git clone https://github.com/jacksongooding/CS193FinalProject
cd CS193FinalProject
./install.sh
```

## Usage
To add elements to the list run ./addtodo.sh while in the directory (or you can add the file to /usr/local/bin/) and run it anywhere. 
Add once syntax has been decidied
To remove an element just press the "x"


## Roadmap

- [x] Add Terminal Based task adding of tasks
- [x] Add a graphical Display of tasks I have to do
- [x] Add graphical controls and make the interface more dynamic
- [ ] Add dynamic color changer for task importance/overdue tasks + instant update after CLI addition

## Author

Jackson, https://github.com/jacksongooding
