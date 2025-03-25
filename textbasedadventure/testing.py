# Testing Code Python
import time
import sys


animation = "Please Press Enter to Continue"
while True:
    # Display the entire phrase
    sys.stdout.write("\r" + animation)
    sys.stdout.flush()
    time.sleep(0.5)  # Pause for half a second

    # Clear the phrase
    sys.stdout.write("\r" + " " * len(animation))
    sys.stdout.flush()
    time.sleep(0.5)  # Pause for half a second
