# Activity 4: Party Roster Manager

MSBA 270 - Python Programming

## About This Project

For this activity, I made a simple RPG character manager using Python and SQLite.

In Week 8, I created a text menu to add, view, and delete characters. In Week 9, I added a GUI using Tkinter, so users can manage their characters with buttons instead of typing menu options.

Both programs use the same database, so the characters are saved even after closing the program.

## Features

- Add characters with a name, HP, level, and class.
- View all saved characters.
- Delete a character by its ID in the text menu or by selecting it in the GUI.
- Show error messages when users enter invalid information.
- Save characters in a SQLite database.
- Use the same character data in both the text menu and GUI.

## Project Files

- `code/roster_db_starter.py` - Week 8 text-menu program.
- `code/roster_gui_starter.py` - Week 9 GUI program.

The programs create a local file called `roster.db` to save character information. This file is not uploaded to GitHub.

## Requirements

- Python 3.10 or newer
- SQLite (`sqlite3`)
- Tkinter (`tkinter` and `ttk`)
- No additional packages required

## How to Run

Open a terminal in the `party_roster` folder.

**Week 8 - Text Menu**

```bash
python code/roster_db_starter.py
```

The menu has four options: Add character, List roster, Delete character, and Quit.

**Week 9 - GUI**

```bash
python code/roster_gui_starter.py
```

A window will open with four input fields, an Add Character button, a character list, and a Delete Selected button.

## Example

For example, I can add a character with these details:

- Name: Luna
- HP: 30
- Level: 2
- Class: Archer

After clicking Add Character, Luna appears in the table. I can select her and click Delete Selected to remove her.

## Skills Practiced

- Using SQLite to save and manage data
- Writing SQL commands such as CREATE TABLE, INSERT, SELECT, and DELETE
- Using functions and loops in Python
- Checking user input with `if` statements and `try/except`
- Creating a GUI with Tkinter
- Connecting buttons to functions
- Updating the character list after adding or deleting data

## Known Limitations

- The program does not have an option to edit a character after adding it.
- The GUI does not have a search feature, so users need to look through the list to find a character.


