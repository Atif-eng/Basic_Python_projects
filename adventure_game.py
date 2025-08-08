def start_game():
    print("Welcome to the adventure game!")
    print("You are standing at the entrance of a dark cave.")
    print("Do you want to:")
    print("A) Enter the cave")
    print("B) Run away")

    choice = input("Choose A or B: ").upper()

    if choice == "A":
        cave_entrance()
    elif choice == "B":
        game_over("You ran away. Game over.")
    else:
        print("Invalid choice. Please choose A or B.")
        start_game()

def cave_entrance():
    print("You have entered the cave.")
    print("It's dark and spooky.")
    print("Do you want to:")
    print("A) Light a fire")
    print("B) Explore the cave")

    choice = input("Choose A or B: ").upper()

    if choice == "A":
        fire_lit()
    elif choice == "B":
        explore_cave()
    else:
        print("Invalid choice. Please choose A or B.")
        cave_entrance()

def fire_lit():
    print("You have lit a fire.")
    print("The cave is now warm and cozy.")
    print("You see a treasure chest in the corner.")
    print("Do you want to:")
    print("A) Open the chest")
    print("B) Leave the chest alone")

    choice = input("Choose A or B: ").upper()

    if choice == "A":
        treasure_found()
    elif choice == "B":
        game_over("You left the treasure behind. Game over.")
    else:
        print("Invalid choice. Please choose A or B.")
        fire_lit()

def explore_cave():
    print("You are exploring the cave.")
    print("You stumble upon a hidden passage.")
    print("Do you want to:")
    print("A) Follow the passage")
    print("B) Go back")

    choice = input("Choose A or B: ").upper()

    if choice == "A":
        passage_found()
    elif choice == "B":
        cave_entrance()
    else:
        print("Invalid choice. Please choose A or B.")
        explore_cave()

def treasure_found():
    print("You found the treasure!")
    print("Congratulations, you won!")
    play_again()

def passage_found():
    print("You followed the passage.")
    print("You found a secret exit.")
    print("Congratulations, you escaped the cave!")
    play_again()

def game_over(message):
    print(message)
    play_again()

def play_again():
    print("Do you want to play again?")
    print("A) Yes")
    print("B) No")

    choice = input("Choose A or B: ").upper()

    if choice == "A":
        start_game()
    elif choice == "B":
        print("Thanks for playing!")
    else:
        print("Invalid choice. Please choose A or B.")
        play_again()

start_game()

