# def greet():
#     print("Hello")
#     print("How are you doing?")
#     print("The weather is nice today.")

# greet()


# def great_with_name(name):  # name parameter
#     print(f"Hello, {name}")
#     print(f"How are you doing {name}?")
#     print("The weather is nice today.") 


# great_with_name("Dante") # here Dante is an argument passed into the great with name function


#
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
]


# user_word = input("Enter in your word: ")
# encoded_word = ""
# decoded_word = ""
# for i in user_word:
#     if i in alphabet:
#         encoded_word += alphabet[(alphabet.index(i) - 5) % 26]
#     else:
#         encoded_word += i

# print(encoded_word)


# for i in encoded_word:
#     if i in alphabet:
#         decoded_word += alphabet[(alphabet.index(i) + 5) % 26]
#     else:
#         decoded_word += i

# print(decoded_word)


answer = input("Yes/No: ")[0].lower()

print(answer)