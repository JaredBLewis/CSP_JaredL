# Jared Lewis, Time of Day Python
import time

print("\n")
print("Hello, and welcome to my program!")
name = input("What is your name?: \n")

current = time.time()
local_time = time.localtime(current)
hour = local_time.tm_hour

if hour < 12:
    print(f"Good morning, {name}!")
elif hour < 18:
    print(f"Good afternoon, {name}!")
else:
    print(f"Good evening, {name}!")