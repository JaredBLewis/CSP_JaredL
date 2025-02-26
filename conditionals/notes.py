# Jared Lewis, Conditionals Notes Python
name = input("Enter your name: ")
#1. What puts something inside of the “if” statement?
if name == "Jared":
    print("Hello Jared!")
else: #<= this happens if the condition is false
    print(f"Hello {name}!")

#2. What do if statements do?
#Checks a condition and if it is true it will do a thing
if name == "Jared":#<= this is a condition
    print("Hello Jared!")#<= this is what it does if the condition is true

#3. What are boolean statements? 
#True or False statements
if name == "Jared": #<= this is a boolean statement it is either true or false.
    print("Hello Jared!")
else: #if the boleab is false, the else statement happens.
    print(f"Hello {name}!")
#4. What do else statements do?

#5. What kind of statement do you use if you have more than 2 needed outcomes?
num = int(input("How many cookies are there?: \n"))

#computers read from top to bottom, check the least likely condition first
if num == 0: #<= if always starts the conditional statement
    print("There are none")
elif num == 1: #everything inbetween should be elif
    print("There is one")
elif num < 4:
    print("There are a couple")
elif num < 10:
    print("There are a few")
else: #<= else always ends the conditional statement
    print("There are many")
#6. What do each of the different symbols mean in conditionals?
# < Less than
# > Greater than
# <= Less than or equal to
# >= Greater than or equal to
# == Equal to
# === *Doesn't exist in Python*
# ! Not

#7. What are the 3 logical operators?
if num < 10 and num >5: #And means both booleans must be true
    print("This is a big single digit number.")

elif num < 10 or num >5: #OR means ONE booleans must be true
    print("This is a single digit number.")

elif not num < 10: #Not changes to check if the boolean is false
    print("This is a not single digit number.")

#8. What are logical operators for?
 #Allows the code to handle more difficult questions... increases complexity

#9. What does a nested conditional statement do?
if num < 10:
    if num == 8:
        print("The number is 8")
    else:
        if num == 4:
            print("There are only enough cookies for me... sorry.")
        else:
            print("The number is less than 10")
else:
    print("The number is greater than 10")
# you can nest as many conditionals as you want, but it is not recommended to go past 3.

#10. How do you write an if statement in C?

#11. How do you write else statements in C?

#12. How do you write elif/ else if statements in C?

#13. How do you write the 3 logical operators in C?
