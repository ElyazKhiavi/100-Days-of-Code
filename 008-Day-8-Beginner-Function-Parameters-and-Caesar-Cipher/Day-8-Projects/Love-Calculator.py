# Love Calculator

# Instructions

# 💪 This is a difficult challenge! 💪

# You are going to write a function called calculate_love_score() that tests the compatibility between two names. To work out the love score between two people:

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.

# 2. Then check for the number of times the letters in the word LOVE occurs.

# 3. Then combine these numbers to make a 2 digit number and print it out.

# e.g.

# name1 = "Angela Yu" name2 = "Jack Bauer"


# 53


def calculate_love_score(name1, name2):
    true = "true"
    love = "love"

    def check(word):
        score = 0
        for i in name1 + name2:
            if i.lower() in word:
                score += 1
        return score

    print(f"Love Score = {check(true)}{check(love)} ")


calculate_love_score(input("Name 1:"), input("Name 2:"))
