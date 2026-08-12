import random
import os
from art import vs, logo
from gameData import data


def get_random():
    return random.choice(list(data.keys()))


def compare_followers(first, second):
    if data[first] > data[second]:
        return "a"
    else:
        return "b"  # if they are equal we will still return second, that means the user still wins the round


def determine_winner():
    first = get_random()
    score = 0
    game_over = False

    while not game_over:
        second = get_random()
        print(f"Compare A: {first} has {data[first]:,} followers.")
        print(vs)
        print(f"Against B: {second}")
        while True:
            choice = input(f"Who has more followers? Type 'A' or 'B': ").lower().strip()
            outcome = compare_followers(first, second)
            if choice == outcome and choice in ["a", "b"]:
                print(f"You're right! Current score: {score}.")
                score += 1
                first = second
                break
            elif choice != outcome and choice in ["a", "b"]:
                os.system("clear")
                print(f"Sorry, that's wrong. Final score: {score}")
                print(
                    f"{first.split(',')[0]} ({data[first]:,}) has more followers then {second.split(',')[0]} ({data[second]:,})"
                )
                game_over = True
                break
            else:
                print("Invalid choice! Please Type 'A' or 'B'.")


print(logo)


def main():
    while True:
        result = determine_winner()

        again = (
            input("Do you want to play again? (y) for Yes, (n) for No: ")
            .lower()
            .strip()
        )
        if again != "y":
            print("Goodbye.")
            break
        os.system("clear")


if __name__ == "__main__":
    main()
