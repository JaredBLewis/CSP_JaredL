# Jared Lewis, Financial Calculator Update Python

def user_input(type):
    return float(input(f"How much is your monthly {type}?: "))

def info(cost, income, type):
    percent = cost/income *100
    print(f"Your {type} is ${cost:.2f} which is {percent}% of your income.")

# print statement that welcomes my user, and tells them what the program does.
print("\n")
print("Hi there, and welcome to my program!")
print("This program will calculate the best way to spend your money.")

# collect user inputs
income = user_input("income")
rent = user_input("rent")
utilities = user_input("utilities")
groceries = user_input("groceries")
transportation = user_input("transportation")

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