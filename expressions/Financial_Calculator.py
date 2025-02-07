# Jared Lewis, Financial Calculater Python

# print statement that welcomes my user, and tells them what the program does.
print("Hi there, and welcome to my program!\n")
print("This program will calculate the best way tp spend your money.\n")
# ask what their income is (variable an input)
income = float(input("How much is your monthly income?:"))

# ask what their rent is (variable an input)
rent = float(input("How much does your monthly rent?:"))

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

# calculate percent income of rent (rent/income *100) (variable)
per_rent = rent/income*100

# calculate percent income of utilities (utilities/income *100) (variable)
per_utilities = utilities/income*100

# calculate percent income of groceries (groceries/income *100) (variable)
per_groceries = groceries/income*100

# calculate percent income of transportation (transportation/income *100) (variable)
per_transportation = transportation/income*100

# calculate percent income of spending (spending/income *100) (variable)
per_spending = spending/income*100

print("\n\n")

# your rent is $XX.XX and which is XX% of your income. (print)
print("The cost for your rent is $",rent,", which is",per_rent,"% of your income.\n")

# your utilities is $XX.XX and which is XX% of your income. (print)
print("The cost of your utilities is $",utilities,", which is",per_utilities,"% of your income.\n")

# your groceries is $XX.XX and which is XX% of your income. (print)
print("The cost for your groceries is $",groceries,", which is",per_groceries,"% of your income.\n")

# your transportation is $XX.XX and which is XX% of your income. (print)
print("The cost for your transportation is $",transportation,", which is",per_transportation,"% of your income.\n")

# your savings is $XX.XX and which is XX% of your income. (print)
print("Your amount of income is $",savings,", which is 10 % of your income.\n")

# your spending is $XX.XX and which is XX% of your income. (print)
print("Your amount for spending is $",spending,", which is",per_spending,"% of your income.\n")