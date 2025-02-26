# Jared Lewis, Old Enough Python

#to vote: 18
#to drive: 16
#to get learner's permit: 15
#to go to school: 5
print("\n")
print("Hello, and welcome to my program!")
print("This program will determeine what you are old enough to do.")
age = int(input("How old are you?: \n"))

if age >= 18:
    print("You are old enough to vote.")
elif age >= 16:
    print("You are old enough to drive.")
elif age >= 15:
    print("You are old enough to get a learner's permit.")
elif age >= 5:
    print("You are old enough to go to school.")
else:
    print("You are really young...")