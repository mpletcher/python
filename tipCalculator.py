#!/usr/bin/python
# Assign the variable total on line 8!

# assign values to variables
meal = float(raw_input("Please enter the meal cost: "))
tax = float(raw_input("Please enter the tax: "))
tip = float(raw_input("Please enter a tip: "))

# Converts tax and tip to decimal
tax = tax / 100
tip = tip / 100

# Finds meal cost
meal = meal + meal * tax

# Finds total cost
total = meal + meal * tip

print("%.2f" % total)

# Leave the program
raw_input("\nPress the enter key to exit.")