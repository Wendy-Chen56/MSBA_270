#!/usr/bin/env python3
"""
Activity 3: RPG Character Forge (STARTER)

TODOs 1-4 (the Character class)
TODOs 5-6 (save/load)

Run the file often to test as you go:
    python code/character_forge_starter.py
"""

SAVE_FILE = "character_save.txt"


class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.level = level
        self.inventory = []
        # TODO 1: Set self.name, self.hp, self.max_hp (same as starting hp),
        # self.level, and self.inventory (start as an empty list).
        

    def take_damage(self, amount):
        self.hp -= amount
        
        if self.hp < 0:
            self.hp = 0
        # TODO 2: Reduce self.hp by `amount`. Don't let it go below 0.
        

    def level_up(self):
        self.level += 1
        self.hp = self.max_hp
        # TODO 3: Increase self.level by 1 and restore self.hp to self.max_hp.
        

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Level: {self.level}")
        print(f"Inventory: {self.inventory}")
        # TODO 4: Print name, hp/max_hp, level, and inventory.
        

    def save_to_file(self, filename):
        # TODO 5: Open `filename` for writing and write self.name, self.hp,
        # and self.level (e.g. one value per line). Use `with open(...)`.
      with open(filename, "w") as file:
                  file.write(self.name + "\n")
                  file.write(str(self.hp) + "\n")
                  file.write(str(self.level) + "\n")
                    


def load_character(filename):
    """Load a saved character from filename, or return None if not found."""

    # TODO 6: Open `filename` for reading inside a try/except FileNotFoundError
    # block. Read back name, hp, and level, and return a new Character built
    # from those values. Return None if the file doesn't exist yet.
    try:
            with open(filename, "r") as file:
                name = file.readline().strip()
                hp = int(file.readline().strip())
                level = int(file.readline().strip())
    
            return Character(name, hp, level)
    
    except FileNotFoundError:
            return None


def main():
    print("=== RPG Character Forge ===\n")

    hero = load_character(SAVE_FILE)

    if hero is None:
        print("No saved character found. Creating a new one!")
        hero = Character("Hero", 100, 1)

    hero.display_stats()

    print("\nHero takes 30 damage.")
    hero.take_damage(30)
    hero.display_stats()

    print("\nHero levels up.")
    hero.level_up()
    hero.display_stats()

    # Week 7 save functionality will be completed later.
    hero.save_to_file(SAVE_FILE)
    print(f"\nCharacter saved to: {SAVE_FILE}")


if __name__ == "__main__":
    main()
    
