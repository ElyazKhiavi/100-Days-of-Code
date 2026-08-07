import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in choices:
            return choice
        print("Invalid choice. Try again.")

def determine_game_winner(player, computer):
    if player == computer:
        print("It's a tie!")
        return "t"
    elif (choices.index(player) + 2) % 3 == choices.index(computer):
        print("You win this round!")
        return "p"
    else:
        print("Computer wins this round!")
        return "c"

def play_round():
    p_choice = player_choice()
    c_choice = get_computer_choice()
    print(f"Player: {p_choice}  –  Computer: {c_choice}")
    return determine_game_winner(p_choice, c_choice)

def match_over(player_score, computer_score, wins_needed):
    """Return True if a player has reached the required wins."""
    if player_score == wins_needed:
        print(f"\n🏆 You win the championship {player_score}-{computer_score}!")
        return True
    elif computer_score == wins_needed:
        print(f"\n💻 Computer wins the championship {computer_score}-{player_score}!")
        return True
    return False

print("Welcome to the Rock‑Paper‑Scissors Championship!")

def main():
    while True:
        # Get valid odd number of wins to become champion
        while True:
            total_wins = input("How many wins to become champion?: ")
            if total_wins.isdigit():
                total_wins = int(total_wins)
                # if total_wins % 2 == 1:   ## ==> we changed my logic now don't need odd number for tie breaker just get the number of wins need 
                #     break
                # else:
                #     print("Please enter an odd number.")
            else:
                print("Invalid input. Enter a number.")

        p_score = 0
        c_score = 0
        round_num = 0

        while True:
            round_num += 1
            print(f"\n--- Round {round_num}: Player {p_score} – Computer {c_score} ---")
            winner = play_round()

            if winner == "p":
                p_score += 1
            elif winner == "c":
                c_score += 1

            if match_over(p_score, c_score, total_wins):
                break

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break
        # if 'y', loop continues

main()