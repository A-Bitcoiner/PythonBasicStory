# Define a flag to track whether the player is in the cave or not
in_cave = True
# Define a flag to track whether the player has the rope
has_rope = False
# Define a flag to track whether the player is in the town or not
in_town = False

# Define the main game loop
while True:
    # Print the current location
    if in_cave:
        print("You are in a dark cave.")
        if not has_rope:
            print("You see a faint light to the north and a deep abyss to the east.")
            print("There is a rope lying on the ground.")
        else:
            print("You see a faint light to the north and a deep abyss to the east.")
    elif not has_rope:
        print(
            "You are in a beautiful forest. You see the entrance to the cave to the south and a deep abyss to the east.")
    elif not in_town:
        print(
            "You are in a beautiful forest. You see the entrance to the cave to the south, a deep abyss to the east, and a town to the east.")
    else:
        print("You are in a bustling town. You see the entrance to the forest to the west and a shop to the north.")

    # Get the player's input
    action = input("What do you do? ")

    # Check if the player wants to go north
    if action == "go north":
        if in_cave:
            in_cave = False
            print("You move towards the light and find yourself in a beautiful forest.")
        elif in_town:
            print("You enter the shop.")
        else:
            print("You are already out of the cave.")
    # Check if the player wants to go east
    elif action == "go east":
        if not has_rope:
            print("You try to cross the abyss, but you fall to your death. Game over!")
            break
        else:
            in_town = True
            print("You use the rope to cross the abyss and enter a town.")
    # Check if the player wants to go south
    elif action == "go south":
        if in_cave:
            print("You are already in the cave.")
        elif in_town:
            print("There is nothing to the south.")
        else:
            in_cave = True
            print("You return to the cave.")
    # Check if the player wants to get the rope
    elif action == "get rope":
        if in_cave:
            has_rope = True
            print("You pick up the rope.")
        else:
            print("There is no rope here.")
    # Check if the player wants to go west
    elif action == "go west":
        if in_town:
            in_town = False
            print("You leave the town and return to the forest.")
        else:
            print("You are already in the forest.")
    # Check if the player wants to quit
    elif action == "quit":
        print("Thanks for playing!")
        break
    # If the input is invalid, print an error message
    else:
        print("I'm sorry, I didn't understand that.")
