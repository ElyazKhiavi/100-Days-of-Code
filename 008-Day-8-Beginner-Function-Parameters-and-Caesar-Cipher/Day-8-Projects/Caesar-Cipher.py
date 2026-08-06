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

characters = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
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
    "-",
    "_",
    "=",
    "+",
    "[",
    "]",
    "{",
    "}",
    "\\",
    "|",
    ";",
    ":",
    "'",
    '"',
    ",",
    ".",
    "<",
    ">",
    "/",
    "?",
    "`",
    "~",
    " ",
]

print(
    """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""
    """"        `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88        
            88             88                          
           00             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP"""
    """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             
"""
)


def caesar_cipher(text, shift, dir):
    txt = ""
    if dir == "decode":
        shift *= -1
    for i in text:
        if i.lower() in alphabet:
            txt += alphabet[(alphabet.index(i.lower()) + shift) % len(alphabet)]
            # txt+=alphabet[alphabet.index(i)+shift] # avoid error by modula
        elif i in characters:
            txt += characters[(characters.index(i) + shift) % len(characters)]
        else:
            txt += i
    if dir == "decode":
        print(f"Decrypted: [{txt}]")
    else:
        print(f"Encrypted: [{txt}]")


print("Welcome to the Cipher Vault.")


def main():
    while True:
        while True:
            direction = input(
                "Encrypt or decrypt your message?\nType 'encode' to encrypt, 'decode' to decrypt: "
            ).lower()
            if direction == "encode" or direction == "decode":
                break
        if direction == "encode":
            text = input("Enter your secret message: ")
            while True:
                shift = input("Choose your shift number: ")
                if shift.isdigit():
                    shift = int(shift)
                    break
            caesar_cipher(text, shift, direction)

        else:
            text = input("Enter the coded message: ")
            while True:
                shift = input("Enter the shift key: ")
                if shift.isdigit():
                    shift = int(shift)
                    break
            caesar_cipher(text, shift, direction)

        again = input("Crack another one? (y/n): ").lower()
        if again == "y":
            print("Back to the vault.")
        else:
            print("Locking the vault. Until next time...")
            break


main()
