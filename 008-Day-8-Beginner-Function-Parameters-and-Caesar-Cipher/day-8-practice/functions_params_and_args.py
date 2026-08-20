def greet():
    print("Hello")
    print("How are you doing?")
    print("The weather is nice today.")


greet()


def greet_with_name(name):  # name parameter
    print(f"Hello, {name}")
    print(f"How are you doing {name}?")
    print("The weather is nice today.")


greet_with_name(
    "Dante"
)  # here Dante is an argument passed into the great with name function


def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")


greet_with("DANTE", "NYC")

greet_with(location="NoWhere", name="Diablo")
