# Try/Except


age = int(
    input("Enter in your age")
)  #  <== this will cause value error if the user enters in something that can not be converted to an integer


while True:
    new_age = input("Enter in your age: ")
    try:
        new_age = int(new_age)
    except ValueError:
        print("Please enter in a valid number.")


    