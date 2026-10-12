# Activity 3: RPG Character Forge

MSBA 270 - Python Programming

## Purpose

The purpose of this activity is to practice object-oriented programming in Python by creating a custom `Character` class.

This activity focuses on understanding classes, objects, attributes, methods, constructors, and object state.

The program creates a simple RPG character with a name, health points, level, and inventory.

---

## Files

- `code/character_forge_starter.py` - the Python program for the Character Forge activity
- `README.md` - project documentation, instructions, and learning notes

---

## Project Structure

```text
activity_3_character_forge/
├── README.md
└── code/
    └── character_forge_starter.py
```

---

## Features

The `Character` class includes the following attributes:

- `name`
- `hp`
- `max_hp`
- `level`
- `inventory`

The Week 6 version includes the following methods:

- `take_damage()` - reduces the character's HP without allowing it to go below 0.
- `level_up()` - increases the character's level by 1 and restores HP to the maximum HP.
- `display_stats()` - displays the character's current information.

Week 7 will add:

- `save_to_file()` - saves character data to a text file.
- `load_character()` - loads character data from a text file.

---

## Python Version

Python 3.x

No external Python packages are required.

---

## How to Run

Open PowerShell or a terminal and navigate to the activity folder.

Run:

```bash
python code/character_forge_starter.py
```

---

## Sample Output

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

Save feature will be completed in Week 7: character_save.txt
```

---

## What I Implemented

For Week 6, I completed TODOs 1-4 of the Character Forge activity.

### TODO 1: `__init__()`

I created the constructor for the `Character` class.

The constructor initializes:

- `name`
- `hp`
- `max_hp`
- `level`
- `inventory`

The inventory starts as an empty list.

Example:

```python
def __init__(self, name, hp, level):
    self.name = name
    self.hp = hp
    self.max_hp = hp
    self.level = level
    self.inventory = []
```

### TODO 2: `take_damage()`

I created the `take_damage()` method.

This method subtracts the damage amount from the character's HP.

I also added a condition so HP cannot go below 0.

Example:

```python
def take_damage(self, amount):
    self.hp -= amount

    if self.hp < 0:
        self.hp = 0
```

### TODO 3: `level_up()`

I created the `level_up()` method.

This method increases the character's level by 1 and restores the character's HP to `max_hp`.

Example:

```python
def level_up(self):
    self.level += 1
    self.hp = self.max_hp
```

### TODO 4: `display_stats()`

I created the `display_stats()` method.

This method displays:

- character name
- current HP and maximum HP
- level
- inventory

Example:

```python
def display_stats(self):
    print(f"Name: {self.name}")
    print(f"HP: {self.hp}/{self.max_hp}")
    print(f"Level: {self.level}")
    print(f"Inventory: {self.inventory}")
```

---

## Challenges I Faced

One challenge was understanding the difference between a class and an object.

I learned that the `Character` class is the blueprint, while `Hero` is an object created from that class.

Another challenge was understanding `self`.

I learned that `self` refers to the current object and allows each method to access or modify the attributes that belong to that object.

I also had to understand how an object's state changes while the program runs.

For example:

- `take_damage()` changes the character's HP.
- `level_up()` changes the character's level.
- `level_up()` also restores the character's HP to `max_hp`.

This helped me understand that object attributes can change when methods are called.

---

## What I Learned

Through this activity, I learned how to:

- Define a class in Python.
- Create objects from a class.
- Use `__init__()` as a constructor.
- Use `self` to access object attributes.
- Store related data inside an object.
- Create methods that change object state.
- Prevent HP from going below 0.
- Restore HP when a character levels up.
- Display the current state of an object.
- Understand the difference between a class and an object.
- Understand the difference between procedural programming and object-oriented programming.

I also learned that a class describes what an object can store and what the object can do.

---

## Connection to Chapter 14

This activity connects to Section 3, Chapter 14 of *Murach's Python Programming*.

The assigned reading was pages 374-413.

Important topics from the reading included:

- class diagrams
- classes and objects
- attributes
- methods
- object creation
- constructors
- `self`
- object state
- object-oriented programming

The Product class example on pages 376-377 helped explain how attributes and methods are grouped together inside a class.

The object creation example beginning on page 378 helped explain how objects are created from a class.

---

## AI Use Note

I used AI as a learning and debugging assistant during this activity.

AI was used to:

- Explain the difference between a class and an object.
- Explain attributes and methods.
- Explain the purpose of `__init__()`.
- Explain how `self` works.
- Help interpret the TODO instructions.
- Help review program output.
- Help test each TODO step by step.
- Help organize the README documentation.

I completed the activity one step at a time and tested the program after making changes.

I made sure I understood the purpose of each part of the code before continuing.

---

## Week 6 Status

Completed:

- TODO 1: `__init__()`
- TODO 2: `take_damage()`
- TODO 3: `level_up()`
- TODO 4: `display_stats()`

Not completed yet:

- TODO 5: `save_to_file()` - Week 7
- TODO 6: `load_character()` - Week 7

The save/load methods remain placeholders in the Week 6 version and will be completed during Week 7.

---

## Replication Notes

To run this activity:

1. Clone or download the repository.
2. Make sure Python 3 is installed.
3. Open a terminal in the project folder.
4. Run:

```bash
python code/character_forge_starter.py
```

No external packages are required.

---

## Course

MSBA 270 - Python Programming

Activity 3: RPG Character Forge