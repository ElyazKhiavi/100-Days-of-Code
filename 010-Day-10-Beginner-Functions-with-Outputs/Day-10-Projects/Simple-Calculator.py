# Simple Calculator
import os


def calculate(first_num, second_number, operation):
    response = None
    if operation == "+":
        response = first_num + second_number
    elif operation == "-":
        response = first_num - second_number
    elif operation == "*":
        response = first_num * second_number
    elif operation == "/":
        response = first_num / second_number
    return response


# def is_float(s):
#     s_no_minus = s.lstrip("-")
#     if (
#         not s_no_minus or s.count("-") > 1
#     ):  # we still have an edge case here there can be multiple minus signs inside the entry and it would pass as float ---2524 this would be a digit! well it is if we are being honest but the conversion turns an error- at this point it would take too much time to fix this but i know that it is there!
#         return None
#     if s_no_minus.count(".") > 1:
#         return None
#     s_no_dot = s_no_minus.replace(".", "", 1)
#     if not s_no_dot or not s_no_dot.isdigit():
#         return None
#     return float(s)


def get_float(queue="First"):
    while True:
        number = input(f"What's the {queue} number?: ")
        try:
            return float(number)
        except ValueError:
            print("Invalid Number! Enter in a number.")


def get_operation():
    while True:
        operation = input(
            "Pick an operation add(+), subtract(-), multiply(*) or divide(/)\n"
        )
        if operation in ["+", "-", "*", "/"]:
            return operation
        else:
            print("Invalid Operation! Try again.")


def main():
    while True:
        outcome = None
        first_num = get_float()
        while True:
            operation = get_operation()
            while True:
                second_number = get_float(queue="Second")
                if second_number == 0 and operation == "/":
                    print("You can't divide by zero!")
                else:
                    break

            outcome = calculate(first_num, second_number, operation)
            print(f"{first_num} {operation} {second_number} = {outcome}")
            first_num = outcome
            redo = input(
                f"Type 'y' to continue calculating with {outcome}, or type 'n' to start a new calculation type 'q' to quite the calculator: "
            ).lower()
            if redo == "q":
                return
            elif redo == "n":
                os.system("clear")
                break


if __name__ == "__main__":
    main()
