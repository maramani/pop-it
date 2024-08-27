from myfunctions import play_game, design_pattern

user_response = input("Do you want to play a logic game with me?\n")

if user_response.lower() in ("yes", "y"):
    print("Ok, let us play")
else:
    print("okay, let us play some other time")
    exit()  # exits the program

print("""Rules of the game:
         We both can iteratively choose a row and remove as many objects as we wish.
         The one who makes the partner to remove the last object is the winner""")

design_pattern()

play_game()
