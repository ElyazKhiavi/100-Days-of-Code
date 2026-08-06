# Password Strength Checker



# Password Strength Checker
# Enter a password (or 'quit' to exit): hello
# Score: 1/5
# Suggestions:
# - Add at least 8 characters
# - Add uppercase letters
# - Add digits
# - Add special characters

# Enter a password (or 'quit' to exit): Hello123!
# Score: 5/5
# Your password is strong!

# Enter a password (or 'quit' to exit): quit
# Goodbye!

# Password Strength Checker

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_upper = [letter.upper() for letter in alphabet]  # built from alphabet NOT  covered by the course yet
alphabet_upper = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_characters = [
    '!','@','#','$','%','^','&','*','(',')','_','+','-','=',
    '[',']','{','}','|',';',':',"'",'"',',','.','<','>','?','/','~','`'
]

def check_password_strength(password):
    score = 0
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_enough_char = len(password) >= 8

    for char in password:
        if char in alphabet_upper:
            has_upper = True
        elif char in alphabet:    
            has_lower = True
        elif char in numbers:
            has_digit = True
        elif char in special_characters:
            has_special = True

    # Build feedback and score
    suggestions = []
    if has_enough_char:
        score += 1
    else:
        suggestions.append("- Add at least 8 characters")
    if has_upper:
        score += 1
    else:
        suggestions.append("- Add uppercase letters")
    if has_lower:
        score += 1
    else:
        suggestions.append("- Add lowercase letters")
    if has_digit:
        score += 1
    else:
        suggestions.append("- Add digits")
    if has_special:
        score += 1
    else:
        suggestions.append("- Add special characters")

    print(f"Score: {score}/5")
    if score == 5:
        print("Your password is strong!")
    else:
        print("Suggestions:")
        for suggestion in suggestions:
            print(suggestion)

print("Password Strength Checker")

def main():
    while True:
        user_password = input("Enter a password (or 'quit' to exit): ")
        if user_password == "quit":
            print("Goodbye!")
            break
        check_password_strength(user_password)

main()


### what i learned here

#     Flags correctly check membership (in, not not in).

#     Scoring starts at 0 and increments, making the logic easier to follow.

#     Suggestions are collected in a list and printed only when needed.

#     elif avoids counting a character in multiple categories (e.g., a letter can’t be both uppercase and lowercase, but using if alone would be fine too – elif is slightly more efficient).