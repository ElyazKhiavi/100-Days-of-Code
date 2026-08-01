# BMI Calculator with Interpretations
# Instructions

#  bmi = weight / (height ** 2)

# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

# If the bmi is under 18.5 (not including), print out "underweight"

# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

# If the bmi is 25 (including) or over, print out "overweight"


print(
    "Welcome to the BMI Calculator.\nThe body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight."
)
weight = float(input("Please enter your weight below (in Kilograms) : "))
height = float(input("Please also enter your height (in Meters):  "))

bmi = round(weight / (height**2), 2)
print(f"Your BMI is: {bmi}")
if bmi < 18.5:
    print("Underweight")
elif 18.5 < bmi < 25:
    print("Normal Weight")
elif bmi > 25:
    print("Overweight")
else:
    print("Obese")
