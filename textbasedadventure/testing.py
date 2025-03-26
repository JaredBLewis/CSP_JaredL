# Testing Code Python
import time

delay = 0.01
#function for game selection
def game_selection():
    # prints the map
    print(map)

    # Game Selection
    message7 = "You are located where it says 'Map'.\n"\
    "Where do you choose to go?\n"\
    "1. Tic-Tac-Toe\n"\
    "2. Hangman\n"\
    "3. Memory\n"\
    "4. Keypad\n"\
    "Enter the number you choose:\n"

    # function to print the message slowly.
    for char in message7:
        print(char, end="")
        time.sleep(delay)


    # Stupid Proofs input
    while True:
        try:
            user_input = int(input())
            if user_input in [1, 2, 3, 4]:
                break
            else:
                print("Invalid Input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 4.")
            continue

    # Collects the user's input
    if user_input == 4:
        print("Please enter the 3-digit code, enter q to return to map")
        code = input()
        if code == "q":
            game_selection()
        elif code != "826":
            print("Incorrect code. Please try again.")
        elif code == "826":
            False
game_selection()

print("this works")