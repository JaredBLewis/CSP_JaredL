import time
import sys
import threading
import os
import random

input_code = 0

code1_int = random.randint(1,9)
code2_int = random.randint(1,9)
code3_int = random.randint(1,9)



code1 = str(code1_int)

code2 = str(code2_int)
code3 = str(code3_int)

code = code1 + code2 + code3
print (code)

# Fancy text functions - Douglas
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def flashing_text(stop_event):
    sys.stdout.write("\033[?25l")  # Hide the cursor
    sys.stdout.flush()
    while not stop_event.is_set():
        sys.stdout.write("\rPress ENTER to continue   ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r                                ")  # Ensure the line is cleared properly
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\033[?25h")  # Show the cursor again
    sys.stdout.flush()

# sets the delay between each character printed
delay = 0.01

# Tick Tack Toe - Jared Lewis
def tic_tac_toe():
    clear_terminal()

    # Dictionary that holds the board
    slot = {
        1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'
    }

    # Function that draws the board
    def draw_board():
        return (f"{slot[1]} | {slot[2]} | {slot[3]}\n"
                f"{slot[4]} | {slot[5]} | {slot[6]}\n"
                f"{slot[7]} | {slot[8]} | {slot[9]}")

    # Welcomes player and draws the board
    print("\n")
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the computer is O")
    print(draw_board())

    # Main game loop
    while True:
        # Player's turn
        while True:
            try:
                player = int(input("Enter a slot (1-9):\n"))
                if player < 1 or player > 9:
                    print("Invalid slot. Try again.")
                    continue
                if slot[player] == 'X' or slot[player] == 'O':
                    print("Slot already taken. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")
                continue
        slot[player] = 'X'

        # Check if user won
        if (slot[1] == slot[2] == slot[3] or slot[4] == slot[5] == slot[6] or slot[7] == slot[8] == slot[9] or
            slot[1] == slot[4] == slot[7] or slot[2] == slot[5] == slot[8] or slot[3] == slot[6] == slot[9] or
            slot[1] == slot[5] == slot[9] or slot[3] == slot[5] == slot[7]):
            if (slot[1] == slot[2] == slot[3] == 'X' or slot[4] == slot[5] == slot[6] == 'X' or
                slot[7] == slot[8] == slot[9] == 'X' or slot[1] == slot[4] == slot[7] == 'X' or
                slot[2] == slot[5] == slot[8] == 'X' or slot[3] == slot[6] == slot[9] == 'X' or
                slot[1] == slot[5] == slot[9] == 'X' or slot[3] == slot[5] == slot[7] == 'X'):
                print("You win!\nThe third digit is", code3, "\n")
                print("Press Enter to return to the map")
                while True:
                    if input() == "":
                        clear_terminal()
                        game_selection()
                        return  # Exit the function after game_selection()
                    else:
                        break

        # Computer's turn
        while True:
            computer = random.randint(1, 9)
            if slot[computer] != 'X' and slot[computer] != 'O':
                slot[computer] = 'O'
                print(draw_board())

                # Check if computer won
                if (slot[1] == slot[2] == slot[3] == 'O' or slot[4] == slot[5] == slot[6] == 'O' or
                    slot[7] == slot[8] == slot[9] == 'O' or slot[1] == slot[4] == slot[7] == 'O' or
                    slot[2] == slot[5] == slot[8] == 'O' or slot[3] == slot[6] == slot[9] == 'O' or
                    slot[1] == slot[5] == slot[9] == 'O' or slot[3] == slot[5] == slot[7]):
                    print("You lost!\n")
                    print("Press Enter to return to the map")
                    while True:
                        if input() == "":
                            clear_terminal()
                            game_selection()
                            return  # Exit the function after game_selection()
                        else:
                            continue
                    
                break

        # Check for tie
        if all(cell == 'X' or cell == 'O' for cell in slot.values()):
            print("It's a tie!")
            print("Press Enter to return to the map")
            while True:
                if input() == "":
                    clear_terminal()
                    game_selection()
                    return  # Exit the function after game_selection()
                else:
                    continue
            break


#Alan De Lara
def hangman():
    clear_terminal()
    # word list  
    words = ["Blood", "dark", "scared", "scream", "drenched", "helpless", "experiment","choking", "crazed", "knife", "chainsaw", "gore", "corpse", "decomposed" ]  
    
    def display_hangman(wrong_attempts):  
        if wrong_attempts == 0:  
            return """  
              ------  
              |      |  
              |        
              |        
              |        
              |        
            __|_________  
            """  
        elif wrong_attempts == 1:  
            return """  
              ------  
              |      |  
              |      O  
              |        
              |        
              |        
            __|_________  
            """  
        elif wrong_attempts == 2:  
            return """  
              ------  
              |      |  
              |      O  
              |      |  
              |        
              |        
            __|_________  
            """  
        elif wrong_attempts == 3:  
            return """  
              ------  
              |      |  
              |      O  
              |     /|
              |        
              |        
            __|_________
            """  
        elif wrong_attempts == 4:  
            return """  
              ------  
              |      |  
              |      O  
              |     /|\\
              |      |  
              |        
            __|_________ 
            """  
        elif wrong_attempts == 5:  
            return """  
              ------  
              |      |  
              |      O  
              |     /|\\
              |      |  
              |     / \\
            __|_________ 
            """  


        return [wrong_attempts]  
    
    def check_guess(letter, chosen_word, guessed_letters):  
        if letter in chosen_word:  
            guessed_letters.append(letter)  
            return True  
        else:  
            return False  
    
    # Main game loop  
    while True:  
        guessed_letters = []  # Reset guessed letters  
        wrong_attempts = 0    # Reset wrong attempts  
        max_attempts = 6      # max attempts  
        chosen_word = random.choice(words)  # Choose a new word  
    
        while wrong_attempts < max_attempts:  # Inner loop for guessing  
            print(display_hangman(wrong_attempts))  # Display hangman  
            display = ''.join(letter if letter in guessed_letters else '_' for letter in chosen_word)  
            print(display)  # Show the current state of the word  
    
            letter = input("Guess a letter: ")  
    
            if len(letter) == 1 and letter.isalpha():  # Validate input  
                if letter in guessed_letters:  
                    print("You've already guessed that letter.")  
                else:  
                    if check_guess(letter, chosen_word, guessed_letters):  
                        print("Good guess!")  
                    else:  
                        wrong_attempts += 1  
                        print("Wrong guess!")  
    
            if set(chosen_word).issubset(set(guessed_letters)):  # Win condition  
                print("Congratulations! You've guessed the word:", chosen_word) 
                print("\n")
                print("The first digit is", code1, "\n")
                print("Press Enter to return to the map")
                while True:
                    if input() == "":
                        clear_terminal()
                        game_selection()
                    else:
                        continue
                break  
            
        if wrong_attempts == max_attempts:  # Loss condition  
            print("Game over! The word was:", chosen_word)
            print("Press Enter to return to the map")
            while True:
                if input() == "":
                    clear_terminal()
                    game_selection()
                else:
                    continue
            break  

#Anthony Petersen
def memory():
    clear_terminal()
    delay = 0.035

    ANinstructions = "This is a memory game that will flash the numbers and you have to repeat them.\n" \
                     "Press Enter to begin.\n"
    ANinstructions2 = "Please enter your answer, and remember to add spaces in between each number: \n"\
                     "HINT: If the flashed numbers where:\n"\
                     "[ 1 ] [ 4 ]\n"\
                     "[ 2 ] [ 5 ]\n"\
                     "[ 3 ] [ 6 ]\n"\
                     "You would enter the answer as '1 4 2 5 3 6'\n"

    def start_game():
        clear_terminal()
        # Generate random numbers for the memory sequence
        ANmemory_1 = random.randint(1, 9)
        ANmemory_2 = random.randint(1, 9)
        ANmemory_3 = random.randint(1, 9)
        ANframes = [
            """  
            [ x ] [ x ]
            [ x ] [ x ]  
            [ x ] [ x ]""",
            f"""  
            [ {ANmemory_2} ] [ {ANmemory_3} ]   
            [ {ANmemory_3} ] [ {ANmemory_1} ]  
            [ {ANmemory_1} ] [ {ANmemory_2} ]""",
            """  
            [ x ] [ x ]    
            [ x ] [ x ]    
            [ x ] [ x ]""",
        ]

        # Display the frames
        for frame in ANframes:
            print(frame)
            time.sleep(2)  # Pause for a moment to show the frame
            os.system("cls" if os.name == "nt" else "clear")  # Clear the screen

        # Return the correct sequence
        return [ANmemory_2, ANmemory_3, ANmemory_3, ANmemory_1, ANmemory_1, ANmemory_2]

    def check_guess(ANuser_input, ANcorrect_guess):
        # Compare the user's input with the correct sequence
        if ANuser_input == ANcorrect_guess:
            print("Well done!")
            return True
        else:
            print("Try again!")
            return False
        
    # Display instructions
    for char in ANinstructions:
        print(char, end="")
        time.sleep(delay)
    input()  # Wait for the user to press Enter

    while True:  # Loop until the user guesses correctly
        ANcorrect_sequence = start_game()  # Display the frames and get the correct sequence
        ANuser_input = input(ANinstructions2).split()  # Get the user's input as a list of strings

        try:
            # Convert input to integers
            ANuser_input = [int(num) for num in ANuser_input]
            if check_guess(ANuser_input, ANcorrect_sequence):  # Check if the guess is correct
                print("Digit #2 is", code2)
                print("Press Enter to return to the map")
                while True:
                    if input() == "":
                        clear_terminal()
                        game_selection()
                        return  # Exit the function after returning to the map
                    else:
                        continue
        except ValueError:
            print("Please enter numbers only!")  # Handle invalid input

# Clear the terminal
clear_terminal()

# functin for keypad
def keypad():
    while True:
        print(code1, code2, code3)
        print("Please enter the 3-digit code, or enter 'q' to return to the map.")
        input_code = input()
        if input_code == "q":
            clear_terminal()
            game_selection()
            return 
        elif input_code != code:
            print("Incorrect code. Try again.")
        elif input_code == code:
            print("Correct code! The door unlocks, and you proceed to the next area.")
            clear_terminal()
            break 

#function for game selection
def game_selection():
    # prints the map
    print(map)

    # Game Selection
    message8 = "You are located where it says 'Map'.\n"\
    "Where do you choose to go?\n"\
    "HINT: The selections may have an answer to the code.\n"\
    "1. Tic-Tac-Toe\n"\
    "2. Hangman\n"\
    "3. Memory\n"\
    "4. Keypad\n"\
    "Enter the number you choose:\n"

    # function to print the message slowly.
    for char in message8:
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

    # Collects the user's input
    if user_input == 1:
        tic_tac_toe()
    elif user_input == 2:
        hangman()
    elif user_input == 3:
        memory()
    elif user_input == 4:
        clear_terminal()
        keypad()

# Calls The game_selection Funtion
game_selection()

print("it worked")