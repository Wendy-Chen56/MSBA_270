# Activity 4: Party Roster Manager

MSBA 270 - Python Programming

## About This Project

For this activity, I built a simple program to manage RPG characters using Python and SQLite.

The program lets users add characters, view the roster, and delete characters. Each character has a name, class, HP, and level.

The character information is saved in a database, so it is still there when the program is closed and opened again.

## Features

- Add a new character with a name, class, HP, and level.
- View all characters saved in the database.
- Delete a character by entering its ID.
- Check for invalid inputs, such as empty names or incorrect numbers.
- Save character information between runs.

## Project Files

- `code/roster_db_starter.py` - The main program for Week 8.
- `code/roster_gui_starter.py` - Starter file for the Week 9 activity.

The program also creates a `roster.db` file to store character information. This file is kept locally and is not uploaded to GitHub.

## Requirements

- Python 3.10 or newer
- Python's built-in `sqlite3` module
- No extra packages needed for Week 8

## How to Run

Open the terminal in the `activity_4_party_roster` folder and enter:

```bash
python code/roster_db_starter.py
```

The program will show four options:

1. Add character
2. List roster
3. Delete character
4. Quit

Enter a number to choose what you want to do.

## Example

For example, I can add a character with these details:

- Name: Mira
- Class: Mage
- HP: 24
- Level: 3

When I choose "List roster," the program shows Mira along with her character ID. I can also use that ID to delete her from the roster.

