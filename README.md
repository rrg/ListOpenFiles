List Open Files
Generates a text list of all the open files in current sublime text window.

Installation
Using Package Control, install "ListOpenFiles"

Or

Open the Sublime Text Packages folder
- OS X: ~/Library/Application Support/Sublime Text 3/Packages/
- Windows: %APPDATA%/Sublime Text 3/Packages/
- Linux: ~/.Sublime Text 3/Packages/
clone this repo
Add keymap for the command

My preferred key binding:
[
    { "keys": ["ctrl+alt+l"], "command": "list_open_files" }
]

Command
list_open_files: Creates a text list of all the open files in Sublime Text.