# End Of Storyline
import time
import sys
import threading
import os
import random

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
delay = 0.05

# Copy and Paste section

# next message
clear_terminal()
message16 = "You fling the door open, not caring for what might be on the other side.\n"\
"If anything, it is probably better than where you came from.\n"\
"You sprint down the new hallway and up a flight of stairs.\n"\
"All the cardio training from Navy Seals manages to help\n"\
"push your adrenalin fuelled body further and faster than ever,\n"\
"but it isn't fast enough...\n"

# function to print the message slowly.
for char in message16:
    print(char, end="")
    time.sleep(delay)

# brief pause for suspense
time.sleep(1)

# next message
message17 = "The creature is hot in pursuit, and you can practically feel it progressing towards you.\n"\
"Closing the distance faster than you would like.\n"\
"Then...\n"\

# function to print the message slowly.
for char in message17:
    print(char, end="")
    time.sleep(delay)

# brief pause for suspense
time.sleep(1)

# next message
message18 = "You see your chance.\n"\
"Just ahead, you see an opening to a large room, and further in the room, is a door with light peeking through the cracks.\n"\
"Not just any light, natural light.\n"\
"You pull any last ounce of strength from your weekend body and push it into your legs.\n"\
"Managing to propel your body the final distance.\n"\
"Never before has time passed so slowly.\n"\
"You can feel the pumping of each stride of your legs,\n"\
"the beat of your heart pumping furiously inside your chest,\n"\
"But worst of all, \n"\

# function to print the message slowly.
for char in message18:
    print(char, end="")
    time.sleep(delay)

# brief pause for suspense
time.sleep(1)

# next message
message19 = "the cold breath,\n"

# function to print the message slowly.
for char in message19:
    print(char, end="")
    time.sleep(delay)

# brief pause for suspense
time.sleep(1)

# next message
message20 = "the thumping legs,\n"

# function to print the message slowly.
for char in message20:
    print(char, end="")
    time.sleep(delay)

# brief pause for suspense
time.sleep(1)

# next message
message21 = "and the grazing touch of spidery fingers,\n"

# function to print the message slowly.
for char in message21:
    print(char, end="")
    time.sleep(delay)

# brief pause for suspense
time.sleep(1)

# next message
message22 = "of the beast, just inches behind you.\n"

# function to print the message slowly.
for char in message22:
    print(char, end="")
    time.sleep(delay)

# brief pause for suspense
time.sleep(3)

# next message
message23 = "You close the distance to the door in the fastest sprint of your life.\n"\
"Slamming into it, and immediately busting it open.\n"\
"As you find yourself outside, you turn to look back.\n"\
"Watching the creature skulk its way back to the heart of its layer, before you collapse onto\n"\
"the cold hard asphalt of an abandoned parking lot.\n"\

# function to print the message slowly.
for char in message23:
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

message24 = "As you come to your senses, you realize the full moon shining, totally oblivious to the\n"\
"traumatizing experience you just endured.\n"\
"You scan your surroundings and spot your car, lying untouched in the parking lot.\n"\
"As you limp towards it, with every step igniting a fire in your legs, you notice a piece of paper\n"\
"pinned to your windshield by the wipers.\n"\
"On it reads the words, 'It was fun to play with you, I look forward to when we meet again.'\n"\
"You crumple the paper, then quickly slide into the front seat of your car, take the set of spare keys from under the\n"\
"car mat inside, and start the engine.\n"\
"You pull out of the parking lot and slam the gas pedal to the floor, putting as much distance\n"\
"between you and the building as possible.\n"\
"\n"

# function to print the message slowly.
for char in message24:
    print(char, end="",)
    time.sleep(delay)

# pause
time.sleep(1)

message25 = "THE END\n"

# function to print the message slowly.
for char in message24:
    print(char, end="",)
    time.sleep(delay)

# waits for the user to press enter - Douglas
stop_event = threading.Event()
thread = threading.Thread(target=flashing_text, args=(stop_event,))
thread.start()

input()
stop_event.set()
thread.join()
clear_terminal()

# Credits
message26 = "Thank you for playing THE UNDERWORLD!\n"\
"If you didn't know, this game took (number) lines of code.\n"\
"If you could let us know that you appreciated our game, it would mean a lot.\n"\
"Once again, thank you, and fairwell.\n"\
"\n"\
"Credits:" \
"Tic-Tac-Toe  = Jared Lewis"
"Hangman      = Alan De Lara\n"\
"Memory       = Anthony Petersen\n"\
"Lock Picking = Douglas London\n"\
"\n"\
"Story        = Jared Lewis\n"\
"Fancy Text   = Douglas London\n"\
"\n"