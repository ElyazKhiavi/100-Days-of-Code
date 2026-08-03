import random
from random import choice

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = [
    "~",
    "`",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "_",
    "-",
    "+",
    "=",
    "{",
    "[",
    "}",
    "]",
    "|",
    ":",
    ";",
    "<",
    ",",
    ">",
    ".",
    "?",
    "/",
]
character = [alphabet, numbers, symbols]
print("Welcome to the PyPassword Generator!")
### with randint
# password = ""
# for i in range(int(input("How Many Characters should the password be?: "))):
#     chosen_category = character[randint(0,len(character)-1)]
#     char=chosen_category[randint(0,len(chosen_category)-1)]
#     password+=str(char)

# print(password)

### with choice this time
# password = ""
# for _ in range(int(input("How many characters should the password be? "))):
#     password += str(choice(choice(character)))
# print("Generated password:\n", password)

### Ask questions from the user about to determine the number of symbols and numbers
password_size = int(input("How many characters should the password be? "))
number_of_symbols = int(input("How many symbols would you like? "))
if number_of_symbols>password_size//3:
    print(f"Too many symbols! You can have at most {password_size // 3}")
    exit()
number_of_numbers = int(input("How many numbers would you like? "))
if number_of_numbers>password_size//3:
    print(f"Too many numbers! You can have at most {password_size // 3}.")
    exit()

rest_of_the_chars = password_size-number_of_symbols-number_of_numbers

password_list = []
for _ in range(number_of_symbols):
    password_list.append(choice(symbols))
for _ in range(number_of_numbers):
    password_list.append(choice(numbers))
for _ in range(rest_of_the_chars):
    password_list.append(choice(alphabet))

password_chars_holder = password_list[:]
### without shuffle
# for _ in password_chars:
#     char = choice(password_chars_holder)
#     password_chars_holder.remove(char)
#     password+=char

### Using .join instead of a for loop
# final_password = ""
# random.shuffle(password_chars_holder)
# for i in password_chars_holder:
#     final_password+=i
# print("Here is your password: \n", final_password)

random.shuffle(password_chars_holder)
print("Here is your password: \n", "".join(password_chars_holder))