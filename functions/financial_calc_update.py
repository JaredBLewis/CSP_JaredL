# Jared Lewis, Financial Calculator Update Python

def input(type):
    return print(input(f"How much is your monthly {type}?:"))

def info(cost, income, type):
    percent = cost/income *100
    print(f"Your {type} is ${cost:.2f} which is {percent}% of your income.")

def w
# print statement that welcomes my user, and tells them what the program does.
print("Hi there, and welcome to my program!\n")
print("This program will calculate the best way to spend your money.\n")
# ask what their income is (variable an input)
income = input("What is your monthly income?:")

# ask what their rent is (variable an input)
rent = float(input("How much does your monthly rent cost?:"))

# ask what their utilities is (variable an input)
utilities = float(input("How much do your monthly utlities cost?:"))

# ask what their groceries is (variable an input)
groceries = float(input("How much do your monthly groceries cost?:"))

# ask what their transportation is (variable an input)
transportation = float(input("How much does your monthly transportation cost?:"))

# claculate savings as 10% of income (income*.1) (variable)
savings = income*.1

# claculate spending as income-savings-rent-utilities-groceries-trensportation (variable)
spending = income-savings-rent-utilities-groceries-transportation

info(rent, income, "rent")
info(utilities, income, "utilities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")