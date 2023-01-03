# Define a flag to track whether the player is in the cave or not
in_cave = True

# Define the main game loop
while True:
  # Print the current location
  if in_cave:
    print("You are in a dark cave. You see a faint light to the north and a deep abyss to the east.")
  else:
    print("You are in a beautiful forest. You see the entrance to the cave to the south.")
  
  # Get the player's input
  action = input("What do you do? ")
  
  # Check if the player wants to go north
  if action == "go north":
    if in_cave:
      in_cave = False
      print("You move towards the light and find yourself in a beautiful forest.")
    else:
      print("You are already out of the cave.")
  # Check if the player wants to go east
  elif action == "go east":
    print("You walk towards the abyss and fall to your death. Game over!")
  # Check if the player wants to go south
  elif action == "go south":
    if in_cave:
      print("You are already in the cave.")
    else:
      in_cave = True
      print("You return to the cave.")
  # Check if the player wants to quit
  elif action == "quit":
    print("Thanks for playing!")
    break
  # If the input is invalid, print an error message
  else:
    print("I'm sorry, I didn't understand that.")
