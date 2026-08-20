# Click to run the final project you will build.
# Welcome to the tip calculator!
# What was the total bill? $124.54
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill?5
# Each person should pay: $27.90

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = float(input("How much tip would you like to give? 10%, 12%, or 15%? "))
# number of people is indeed a whole number
people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
each_person = round(total / people, 2)

print(f"Each person should pay: ${each_person}")
