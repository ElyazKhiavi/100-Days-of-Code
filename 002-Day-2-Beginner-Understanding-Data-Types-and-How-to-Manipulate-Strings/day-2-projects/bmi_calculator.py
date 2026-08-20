# bmi is equal to the person's weight divided by the person's height squared.
# BMI Category	BMI Range
# Underweight	Below 18.5
# Healthy Weight	18.5 to 24.9
# Overweight	25.0 to 29.9
# Obesity	30.0 or greater
print('Welcome to the BMI Calculator.\nThe body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight.')
weight = float(input("Please enter your weight below (in Kilograms) : "))
height = float(input("Please also enter your height (in Meters):  "))

bmi = weight/(height*height)
print(f'\nYour BMI is: {bmi}')
print('Below 18.5     → Underweight')
print('18.5 – 24.9    → Healthy Weight')
print('25.0 – 29.9    → Overweight')
print('30.0+          → Obesity')