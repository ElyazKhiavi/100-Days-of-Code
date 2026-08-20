number_to_check = int(input("Please enter a whole number: "))
remainder = number_to_check % 2

print(f"Remainder is {remainder}")
if remainder == 0:
    print("It's an Even Number.")
else:
    print("It's an Odd Number.")
