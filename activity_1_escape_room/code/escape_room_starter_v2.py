def check_key(inventory):
    """Check if the player has a key."""
    for item in inventory:
        if item == "key":
            return True
    return False


def room_one(inventory):
    """Room 1: Haunted Library."""

    # TODO 1: Print a short description of the starting room.
    # Example: "You wake up in a dusty library. There is a door to the LEFT
    # and a desk in front of you."
    
    
    print("\n=== Haunted Library ===")
    print("You wake up in a dark, dusty library.")
    print("You hear footsteps outside the room...")
    print("There is a locked door and an old desk.")

    choice = input("Do you check the 'door' or the 'desk'? ").lower()

    if choice == "door":
        key = check_key(inventory)

        if key:
            print("\nYou put the key into the lock...")
            print("CLICK!")
            print("The door slowly opens.")
            print("Congrats! You escaped Room 1!")
            room = "room_two"

        else:
            print("\nThe door is locked!")
            print("Maybe you should search the room...")
            room = "room_one"

    elif choice == "desk":
        key = check_key(inventory)

        if key:
            print("\nYou search the desk again.")
            print("There is nothing else here.")
            print("You already have the key!")

        else:
            print("\nYou slowly open the old desk...")
            print("You find a small golden key!")
            inventory.append("key")

        room = "room_one"

    elif choice == "quit":
        room = "quit"

    else:
        print("\nI don't understand that choice.")
        room = "room_one"

    return room


def main():
    print("=== ESCAPE ROOM ===")
    print("Can you escape the haunted library?")
    print("Type 'quit' at any time to give up.\n")

    inventory = []

    current_room = "room_one"


    # TODO 2: Set the loop condition so the game keeps running until the
    # player escapes or quits. Hint: use a `playing` boolean flag.
    
    
    
    playing = True

    while playing:
        if current_room == "room_one":
            current_room = room_one(inventory)

        elif current_room == "room_two":
            print("\nYou made it to Room 2...")
            playing = False

        elif current_room == "quit":
            print("\nYou gave up. The library keeps its secrets...")
            playing = False


if __name__ == "__main__":
    main()
    
    
# ============================================================
# Two Things That Can Break My Program
# ============================================================

# 1. Invalid or Unexpected User Input
# One thing that can break the expected flow of my program is
# invalid or unexpected user input. My program asks the player
# to enter choices such as "door" or "desk". If the player
# misspells a choice, such as typing "dor" instead of "door",
# the program will not recognize the intended command.
# I use .lower() to handle capitalization, but this does not
# correct spelling mistakes or unexpected characters.

# 2. Extra Spaces in User Input
# Another thing that can break the expected flow of my program
# is entering extra spaces. For example, if the player types
# "door " with a space after the word, the program will not
# recognize it as "door". The .lower() method only changes
# uppercase letters to lowercase letters; it does not remove
# extra spaces. I could improve this later by cleaning the
# user's input before checking the choice.