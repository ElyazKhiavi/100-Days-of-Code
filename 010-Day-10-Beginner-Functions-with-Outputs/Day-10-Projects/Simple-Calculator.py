# Simple Calculator
import os

operations = ["+", "-", "*", "/"]


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
    print(f"{first_num} {operation} {second_number} = {response}")
    return response


def is_float(s):
    s_no_minus = s.lstrip("-")
    if (
        not s_no_minus or s.count("-") > 1
    ):  # we still have an edge case here there can be multiple minus signs inside the entry and it would pass as float ---2524 this would be a digit! well it is if we are being honest but the conversion turns an error- at this point it would take too much time to fix this but i know that it is there!
        return None
    if s_no_minus.count(".") > 1:
        return None
    s_no_dot = s_no_minus.replace(".", "", 1)
    if not s_no_dot or not s_no_dot.isdigit():
        return None
    return float(s)


def main():
    while True:
        outcome = None
        while True:
            first_num = input("What's the first number?: ")
            if is_float(first_num) is not None:
                first_num = float(first_num)
                break
            else:
                print("Invalid! Enter in a number")
        while True:
            while True:
                operation = input(
                    "Pick an operation add(+), subtract(-), multiply(*) or divide(/)\n"
                )
                if operation in operations:
                    break
                else:
                    print("Invalid Operation!")

            while True:
                second_number = input(
                    "What's the next number?: "
                )  ## Pay attention to zero division Error
                if is_float(second_number) is not None:
                    second_number = float(second_number)
                    if operation == "/" and second_number == 0:
                        print("You can't divide by zero!")
                    else:
                        break
                else:
                    print("Invalid! Enter in a number")

            outcome = calculate(first_num, second_number, operation)
            first_num = outcome
            redo = input(
                f"Type 'y' to continue calculating with {outcome}, or type 'n' to start a new calculation type 'q' to quite the calculator: "
            ).lower()
            if redo == "q":
                return
            elif redo == "n":
                os.system("clear")
                break


main()
