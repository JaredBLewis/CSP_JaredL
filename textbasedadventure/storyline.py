# Jared Lewis, Storyline
import time

delay = 0.01

message = "Welcome user...\n\
The game you are about to play is a text based adventure game.\n\
This game will test your skills through a serios of minigames.\n\
May I welcome you to...\n\
\n\
THE UNDERWORLD\n\
created by:\n\
Alan De Lara\n\
Anthony Peterson\n\
Douglas London\n\
Jared Lewis\n\
"

for char in message:
    print(char, end="")
    time.sleep(delay)