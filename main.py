# Define flags to track the player's location and inventory
in_cave = True
has_rope = False
in_town = False
in_shop = False
in_forest = False

# Define the main game loop
while True:
    # Print the current location
    if in_cave:
        location = "cave"
    elif in_town:
        location = "town"
    elif in_shop:
        location = "shop"
    elif in_forest:
        location = "forest"

    print(f"You are in a {location}.")

    if location == "cave":
        if not has_rope:

            print("There is a rope lying on the ground.")
            print("You see a faint light to the north.")
        else:
            print("You see a faint light to the north.")
    elif location == "forest":
        if has_rope:
            print("You see the entrance to the cave to the south, a deep abyss to the east, and beyond the abyss is a town.")
        else:
            print("You see the entrance to the cave to the south and a deep abyss to the east.")
    elif location == "town":
        print("You look around the small town. Beyond the abyss you see the entrance to the forest to the west and a shop to the north.")

    # Get the player's input
    action = input("What do you do? ")

    # Check if the player wants to go north
    if action == "go north":
        if location == "cave":
            in_cave = False
            print("You move towards the light and find yourself in a beautiful forest.")
            in_forest = True
        elif location == "town":
            print("You enter the shop. A trader named Zach greets you.")
            in_town = False
            in_shop = True
        else:
            print("You are already out of the cave.")
    # Check if the player wants to go east
    elif action == "go east":
         if location == "cave":
             print("There is a cave wall to the east, you cannot go further east.")
         elif location == "forest":
            if not has_rope:
                print("You try to cross the abyss, but you fall to your death. Game over!")
                break
            else:
                in_town = True
                print("You use the rope to cross the abyss and enter a town.")
         else:
            print("There is nothing to the east.")
    # Check if the player wants to go south
    elif action == "go south":
        if location == "cave":
            print("You are already in the cave and cannot go further south.")
        elif location == "town":
            print("There is nothing to the south.")
        elif location == "shop":
            print("You exit the shop. Zach waves you goodbye as he begins another 100x leveraged trade.")
            in_shop = False
            in_town = True
        else:
            in_cave = True
            print("You return to the cave.")
    # Check if the player wants to get the rope
    elif action == "get rope" or action == "pick up rope":
        if location == "cave":
            has_rope = True
            print("You pick up the rope.")
        else:
            print("There is no rope here.")
    # Check if the player wants to go west
    elif action == "go west":
        if location == "town":
            in_town = False
            print("You leave the town and return to the forest.")
        elif location == "forest":
            print("You are already in the forest.")
        elif location == "cave":
            print("There is a cave wall west, you cannot go further.")
    # Check if the player wants to quit
    elif action == "quit":
        print("Thanks for playing!")
        break
