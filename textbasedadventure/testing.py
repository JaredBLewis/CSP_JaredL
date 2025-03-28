# Testing Code Python

# Text Based Adventure Storyline
import time
import sys
import threading
import os
import random

# Where the story starts
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

# Chapter 2 - Jared
def lock_picking():
    message14 = "Chapter 2:\n"\
    "THE BEAST\n"\
    "\n"


    # function to print the message slowly.
    for char in message14:
        print(char, end="", flush=True)
        time.sleep(delay)


    # waits for the user to press enter - Douglas
    stop_event = threading.Event()
    thread = threading.Thread(target=flashing_text, args=(stop_event,))
    thread.start()


    input()
    stop_event.set()
    thread.join()
    clear_terminal()


    # next message - Jared
    message15 = "The pounding of the supernatural thing on the plate of metal interrupts your brief moment of silence.\n"\
    "You dash to the trapdoor in the center of the room,\n"\
    "and fumble with the key as you try to jam it into the old and tarnished lock.\n"\
    "With shaking hands you manage to twist the key, and you quickly slide it off and fling open the hatch in the floor.\n"\
    "You jump down to the bottom of the stairs that are revealed, and sprint down the corridor.\n"\
    "To your dismay, you find another door, securely padlocked.\n"\
    "Frantically, you look around, and spy a few pins.\n"\
    "You have one chance of survival...\n"\
    "YOU HAVE TO PICK THE LOCK!\n"\


    # function to print the message slowly.
    for char in message15:
        print(char, end="")
        time.sleep(delay)


    # Lock Picking Game - Douglas
    time.sleep(3)
    clear_terminal()
    low = 1
    high = 6
    guess = 0
    num1 = random.randint(low, high)
    num2 = random.randint(low, high)
    num3 = random.randint(low, high)
    num4 = random.randint(low, high)

    correct_answer = [str(num1), str(num2), str(num3), str(num4)]
    correct_count = 0
    wrong_count = 0
    time_limit = 120  # Set the time limit in seconds
    time_up = False  # Flag to indicate if time is up

    # Timer function
    def timer():
        nonlocal time_up
        time.sleep(time_limit)
        time_up = True

    # Start the timer thread
    timer_thread = threading.Thread(target=timer)
    timer_thread.start()

    print("Correct Place: lists the amount of correct numbers in the correct placement.")
    print("Wrong Place: lists the amount of correst numbers in the wrong placement.")
    print("Find the correct numbers and their placement to pick the lock.")
    print("BUT YOU MUST HURRY!")
    print("Only "+str(time_limit)+" seconds until the Beast breaks in!\n")

    while guess == 0:
        if time_up:
            print("The Beast breaks down the door and drags you off, you are never heard of again.")
            print("Press ENTER to retry.")
            input()
            clear_terminal()
            return  # Exit the function if time is up

        if correct_count == 4:
            print("KA_KLUNK!")
            guess = 1
            time.sleep(2)
            return

        user_input = input("Enter your guess (4 digits between 1 and 6):\n")

        if len(user_input) != 4:
            print("Please enter exactly 4 characters.")
            continue

        correct_count = 0
        wrong_count = 0

        correct_positions = [False, False, False, False]
        wrong_positions = [False, False, False, False]
        temp_correct_answer = correct_answer.copy()

        for index in range(4):
            if user_input[index] == correct_answer[index]:
                correct_count += 1
                correct_positions[index] = True
                temp_correct_answer[index] = None
        for index in range(4):
            if not correct_positions[index]:
                for compare_index in range(4):
                    if not correct_positions[compare_index] and user_input[index] == str(temp_correct_answer[compare_index]) and temp_correct_answer[compare_index] is not None:
                        wrong_count += 1
                        temp_correct_answer[compare_index] = None

        print(f"Correct Place: {correct_count}, Wrong Place: {wrong_count}")

    # Stop the timer thread if the user succeeds
    time_up = True
    timer_thread.join()

    # Success message
    print("You successfully picked the lock!")
    print("Press Enter to continue.")
    input()
    clear_terminal()


    print(f"Correct: {correct_count}, Wrong: {wrong_count}")
       
# Calls the lock picking game
lock_picking()
