# Activity 3: RPG Character Forge

**Course:** MSBA 270 – Python Programming  
**Project:** Activity 3: RPG Character Forge  
**Language:** Python 3  
**Status:** Completed (Week 6 and Week 7)

## Project Overview

RPG Character Forge is a command-line Python program that demonstrates object-oriented programming through a simple role-playing game character. The program creates or loads a character, shows its statistics, applies damage, increases its level, and saves the updated character to a text file for future runs.

The project combines **Week 6 (Character class, TODOs 1–4)** with **Week 7 (file persistence, TODOs 5–6)**.

## Features

- Create a character with a name, health points (HP), level, and inventory.
- Display current HP, maximum HP, level, and inventory.
- Apply damage without letting HP drop below zero.
- Level up by one and restore HP to its maximum.
- Save the character's name, current HP, and level in `character_save.txt`.
- Load saved character information when the program starts.
- Create a default character when no saved file exists.

## Project Structure

```text
activity_3_character_forge/
├── README.md
├── KEY_TAKEAWAYS.md
└── code/
    └── character_forge_starter.py
```

The program generates `character_save.txt` in the **current working directory** when it saves a character. The save file is runtime output and does not need to be committed to GitHub.

## Python Concepts Demonstrated

| Concept | Implementation |
|---|---|
| Classes and objects | `Character` class and `hero` instance |
| Constructor | `__init__()` initializes attributes |
| Instance methods | `take_damage()`, `level_up()`, `display_stats()`, `save_to_file()` |
| Conditional logic | HP cannot go below zero; missing save creates a default character |
| File I/O | `open()`, `write()`, `readline()` |
| Exception handling | `FileNotFoundError` when loading an absent save |
| Type conversion | `str()` when saving numbers; `int()` when loading |

## How the Program Works

1. `main()` calls `load_character(SAVE_FILE)`.
2. If no save file is found, it creates `Character("Hero", 100, 1)`.
3. The character's current statistics are displayed.
4. The character takes 30 damage, and its statistics are shown again.
5. The character levels up, restoring its HP to `max_hp`.
6. The program saves the updated character information to `character_save.txt`.

**Save format:** three lines containing the character's name, current HP, and level. The current implementation does not save inventory or a separate maximum-HP value; a loaded character initializes `max_hp` from the saved HP.

## Requirements

- Python 3.x
- No external packages required

## How to Run

From the repository root:

```bash
cd activity_3_character_forge
python code/character_forge_starter.py
```

Or clone the repository first:

```bash
git clone https://github.com/Wendy-Chen56/MSBA_270.git
cd MSBA_270/activity_3_character_forge
python code/character_forge_starter.py
```

## Example Output

**First run (no existing save file):**

```text
=== RPG Character Forge ===

No saved character found. Creating a new one!
Name: Hero
HP: 100/100
Level: 1
Inventory: []

Hero takes 30 damage.
Name: Hero
HP: 70/100
Level: 1
Inventory: []

Hero levels up.
Name: Hero
HP: 100/100
Level: 2
Inventory: []

Character saved to: character_save.txt
```

**Generated save file:**

```text
Hero
100
2
```

On the next run, the program loads the saved character at Level 2, applies damage, levels up to Level 3, and updates the file.

## Implementation Status

| Week | Scope | Status |
|---|---|---|
| Week 6 | TODOs 1–4: character attributes and methods | Complete |
| Week 7 | TODO 5: save character data | Complete |
| Week 7 | TODO 6: load character data | Complete |

