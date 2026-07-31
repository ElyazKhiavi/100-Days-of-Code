
# Type Conversion
print(len(str(1223)))  # 4

print(int("1234") + int("5678"))  # 6912
print(float(123))

print(bool("Sam"))  # True
print(bool(""))  # False
print(bool(False))  # False
print(bool(123))  # True
print(bool(0))  # False

# print(int("same"))  # ValueError: invalid literal for int() with base 10: 'same'


print("Number of Letters in your name: " + str(len(input('Enter Your Name: ')))) # No Errors
