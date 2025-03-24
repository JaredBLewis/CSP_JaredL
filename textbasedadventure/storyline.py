# Jared Lewis, Storyline
import time

# sets the delay between each character printed
delay = 0.035

message = "Welcome user...\n"\
"The game you are about to play is a text based adventure game.\n"\
"This game will test your skills through a series of minigames.\n"\
"May I welcome you to...\n"\
"\n"\
"THE UNDERWORLD\n"\
"created by:\n"\
"Alan De Lara\n"\
"Anthony Peterson\n"\
"Douglas London\n"\
"Jared Lewis\n"\
"\n"\
"Please Press Enter to Continue"

# function to print the message with a delay.
for char in message:
    print(char, end="")
    time.sleep(delay)