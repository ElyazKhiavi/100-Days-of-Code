import random

number = None


def pick_random_number():
    return random.randint(1, 100)


def pick_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Invalid! Choose again!")


def ask_user_for_number():
    while True:
        user_number = input("Make a guess: ").strip()
        try:
            return int(user_number)
        except ValueError:
            print("Invalid Guess! Enter in a number.")


def compare_input(user_input, actual_number):
    if user_input > actual_number:
        return "high"
    elif user_input < actual_number:
        return "low"
    else:
        return "equal"


def play_game():
    global number
    number = pick_random_number()
    print("I'm thinking of a number between 1 and 100.")
    lives = pick_difficulty()
    while lives != 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guessed_number = ask_user_for_number()
        outcome = compare_input(guessed_number, number)
        if outcome == "high":
            print("Too High!")
            print("Guess again.")
        elif outcome == "low":
            print("Too Low!")
            print("Guess again.")
        else:
            return "win"
        lives -= 1
    return "lose"

print("Welcome to the Number Guessing Game!")


def main():
    while True:
        result = play_game()

        if result == "win":
            print(f"You got it! The answer was {number}.")
        else:
            print(f"You ran out of lives, You lose! The answer was {number}.")

        guess_again = input("Do you want to go again? (y)/(n): ").strip().lower()
        if guess_again != "y":
            print("Goodbye...")
            break


if __name__ == "__main__":
    main()
