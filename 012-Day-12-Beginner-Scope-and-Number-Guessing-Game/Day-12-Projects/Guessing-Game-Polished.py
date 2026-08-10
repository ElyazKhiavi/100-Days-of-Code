### The Polished version

import random

# ------------------------------------------------------------
# Number Guessing Game
# ------------------------------------------------------------
# The computer picks a random number between 1 and 100.
# The player chooses easy (10 attempts) or hard (5 attempts).
# After each guess, the game says "Too high." or "Too low."
# The game ends when the player guesses correctly or runs out of attempts.
# ------------------------------------------------------------


def pick_random_number():
    """Return a random integer between 1 and 100."""
    return random.randint(1, 100)


def pick_difficulty():
    """
    Ask the player to choose a difficulty.
    Returns the number of attempts: 10 for easy, 5 for hard.
    Keeps asking until a valid choice is entered.
    """
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Invalid choice! Please type 'easy' or 'hard'.")


def ask_user_for_number():
    """
    Prompt the player to enter a guess.
    Keeps asking until a valid integer is provided.
    """
    while True:
        user_input = input("Make a guess: ").strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid guess. Please enter a whole number.")


def compare_input(user_guess, actual_number):
    """
    Compare the player's guess with the secret number.
    Returns 'high', 'low', or 'equal'.
    """
    if user_guess > actual_number:
        return "high"
    elif user_guess < actual_number:
        return "low"
    else:
        return "equal"


def play_game():
    """
    Run one complete round of the guessing game.
    Returns 'win' if the player guesses correctly,
    or 'lose' if attempts run out.
    """
    number = pick_random_number()   # secret number for this round
    print("\nI'm thinking of a number between 1 and 100.")

    # Set number of attempts based on difficulty
    attempts = pick_difficulty()

    # Game loop – continue while the player still has attempts
    while attempts > 0:
        print(f"\nYou have {attempts} attempt(s) remaining to guess the number.")
        guessed = ask_user_for_number()

        result = compare_input(guessed, number)

        if result == "high":
            print("Too high.")
            print("Guess again.")
        elif result == "low":
            print("Too low.")
            print("Guess again.")
        else:
            # Exact match – player wins
            return "win", number

        attempts -= 1   # use up one attempt

    # No attempts left → player loses
    return "lose", number


def main():
    """Main menu – lets the player play multiple rounds."""
    print("Welcome to the Number Guessing Game!")

    while True:
        outcome, secret = play_game()

        if outcome == "win":
            print(f"\n🎉 You got it! The answer was {secret}.")
        else:
            print(f"\n😞 You ran out of attempts. You lose! The number was {secret}.")

        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


# Run the game if this file is executed directly
if __name__ == "__main__":
    main()