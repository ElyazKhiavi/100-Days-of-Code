import random

# ------------------------------------------------------------
# DECK (infinite – cards are never removed)
# ------------------------------------------------------------
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def pick_a_card():
    """Return a random card from the deck."""
    return random.choice(cards)


# ------------------------------------------------------------
# GLOBAL HANDS (reset each new round)
# ------------------------------------------------------------
player_cards = []
computer_cards = []


def deal_starting_hands():
    """Clear hands and deal two cards to each."""
    global player_cards, computer_cards
    player_cards = [pick_a_card(), pick_a_card()]
    computer_cards = [pick_a_card(), pick_a_card()]


def sum_cards(entered_cards):
    if sum(entered_cards) > 21:
        if 11 in entered_cards:
            entered_cards[entered_cards.index(11)] = 1
    return sum(entered_cards)


def show_hands(hide_dealer=True):
    """
    Print hands and scores.
    When hide_dealer is True, only the dealer’s first card is shown.
    """
    player_sum = sum_cards(player_cards)
    computer_sum = sum_cards(computer_cards)
    print(f"\nYour hand: {player_cards}  →  Score: {player_sum}")

    if hide_dealer:
        # Show only one card; score is unknown
        print(f"Dealer hand: [{computer_cards[0]}, ?]")
    else:
        # Reveal full hand after player stands
        print(f"Dealer hand: {computer_cards}  →  Score: {computer_sum}")


def dealer_play():
    """Dealer draws cards until score >= 17."""
    while sum_cards(computer_cards) < 17:
        computer_cards.append(pick_a_card())


def check_winner():
    """
    Decide the result after the player has stood.
    Priority: dealer 21 beats everything, then player 21, busts, etc.
    Returns 'win', 'lose', or 'draw'.
    """
    p_score = sum_cards(player_cards)
    d_score = sum_cards(computer_cards)

    # 1. Dealer has 21 → player loses (even if player also has 21)
    if d_score == 21:
        return "lose"

    # 2. Player has 21 and dealer does NOT → player wins
    if p_score == 21:
        return "win"

    # 3. Player bust (should be caught earlier, but safety)
    if p_score > 21:
        return "lose"

    # 4. Dealer bust
    if d_score > 21:
        return "win"

    # 5. Compare scores
    if p_score > d_score:
        return "win"
    elif p_score < d_score:
        return "lose"
    else:
        return "draw"


# ------------------------------------------------------------
# SINGLE ROUND OF BLACKJACK
# ------------------------------------------------------------
def play_round():
    """Run one game and return the outcome ('win', 'lose', 'draw')."""
    deal_starting_hands()

    # Show initial hands (dealer card hidden)
    show_hands(hide_dealer=True)

    # ---- Player's turn ----
    while True:
        # Ask for hit or stand (s = stand)
        choice = input("\n(h)it or (s)tand? ").strip().lower()

        if choice == "h":
            player_cards.append(pick_a_card())
            show_hands(hide_dealer=True)  # still hide dealer card

            # Immediately check for bust
            if sum_cards(player_cards) > 21:
                print("You busted! 😞")
                return "lose"
        elif choice == "s":
            break
        else:
            print("Please type 'h' for hit or 's' for stand.")

    # ---- Dealer's turn ----
    print("\n--- Dealer's turn ---")
    dealer_play()
    show_hands(hide_dealer=False)  # now reveal the hidden card

    # ---- Determine winner ----
    return check_winner()


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------
def main():
    print("♠️  Welcome to Blackjack! ♣️")
    while True:
        result = play_round()

        if result == "win":
            print(">>> You win! 🎉")
        elif result == "lose":
            print(">>> You lose. 😢")
        else:
            print(">>> It's a draw. 🤝")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
