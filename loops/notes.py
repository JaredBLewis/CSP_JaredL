# Jared Lewis, Loops Notes Python

# 1. What is a loop? 
    #A loop is a way to repeat a block of code until a condition is met.#a section of code that repeats multiple times.
# 2. What are the two types of loops?
    #for lops
nums = [12,3,66,7,3,3,2]

for num in nums:
    print(num)

#while loop
x =0

while x < 10:
    print(x)
    x += 1
# 3. What is iteration?
    #That specific instance of the loop
    #Iteration is the amount of times you're looping through

# 4. What are lists? 
    nums = [1,2,3,4,5,6,7,6]
    siblings = ["Ty", "Kaden", "Nephi", "Abish", "Jared", "Daniel", "Nathan", "Noah", "Elijah", "Pearl"]
    print(nums) #prints whole list is ugly
    print(siblings[4]) #prints first item in list

    siblings[4] = "Jared"
    siblings.pop(5)
    siblings.insert(2, "Janice")
    siblings.insert(2, ["Joe", "Noah", "Zee"])
    print(siblings)


# 5. How do you make lists in python? 
    #step 1: use brackets
    #step 2: put in the items you want to be in the list
    #step 3: seperate each item with a comma

# 6. How do you make for loops in python? 
    for sibling in siblings:
        print(sibling)

    for x in range(1, 6, 2):
        print("Duck")

# 7. How do you make while loops in python?
    import random 
    x = 1 # variable to keep count of iteration
    goose = random.randint(1, 20)

    while x <= 20:
        if x == goose:
            print("Goose!")
            break #tells the loop to stop
        else:
            print("Duck")
        x+= 1

    #continue moves on the the next iteration without finishing