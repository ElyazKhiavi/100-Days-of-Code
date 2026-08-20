import random
import os
from art import vs, logo
from gameData import data


# Store the list of names once for faster random selection
NAMES = list(data.keys())


def get_random():
    """Return a random name from the data dictionary."""
    return random.choice(NAMES)


def compare_followers(first, second):
    """
    Compare follower counts.
    Returns 'a' if first has more followers, otherwise 'b'.
    If equal, returns 'b' (user wins by guessing B).
    """
    if data[first] > data[second]:
        return "a"
    else:
        return "b"


def determine_winner():
    """
    Run one full round of the Higher‑Lower game.
    Prints the logo, runs the comparison loop, and displays the final score.
    """
    print(logo)                      # show logo at the start of the game
    first = get_random()             # initial first candidate
    score = 0
    game_over = False

    while not game_over:
        second = get_random()        # pick a new second candidate
        print(f"\nCompare A: {first} has {data[first]:,} followers.")
        print(vs)
        print(f"Against B: {second}")

        # Get a valid user choice
        while True:
            choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
            if choice in ["a", "b"]:
                break
            print("Invalid choice! Please type 'A' or 'B'.")

        outcome = compare_followers(first, second)

        if choice == outcome:
            # Correct guess
            score += 1
            print(f"You're right! Current score: {score}.")
            first = second          # second becomes the next 'first'
        else:
            # Wrong guess – game over
            print(f"Sorry, that's wrong. Final score: {score}")
            # Show the correct comparison (using .split(',')[0] to get just the name)
            print(f"{first.split(',')[0]} ({data[first]:,}) has more followers than {second.split(',')[0]} ({data[second]:,})")
            game_over = True


def main():
    """Main game loop – offers replay."""
    while True:
        determine_winner()

        again = input("\nDo you want to play again? (y) for Yes, (n) for No: ").strip().lower()
        if again != "y":
            print("Goodbye.")
            break
        os.system("clear")   # clear screen for a fresh round


if __name__ == "__main__":
    main()