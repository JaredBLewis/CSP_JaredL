#Jared Lewis, Silly Sentences Python
print("\n")
print("Hello, and welcome to Silly sentance Creator!\n")

color = input("Please enter a single color: ").strip().lower()
name = input("Please enter a male name: ").strip().lower().capitalize()
vehicle = input("Please enter a single type of vehicle: ").strip().lower()
animal = input("Please enter an animal: ").strip().lower()
famous_person = input("Please enter the first name of a famous person: ").strip().lower().capitalize()

print("Here is your silly sentance: \n")
print("It was a " + color + " day when " + name + " decided to take a ride in his " + vehicle + ". Then he saw a " + animal + " chasing " + famous_person + " down the street. \n")