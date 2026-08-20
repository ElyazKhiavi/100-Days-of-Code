# Blackjack game
import random
import os

os.system("clear")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)

def computer_card_fix():
    while sum(computer_cards) < 17:
        computer_cards.append(deal_card())


def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1

    return sum(hand)



user_cards = [deal_card(), deal_card()]
computer_cards = [deal_card(), deal_card()]
game_over=False


user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"Your cards: {user_cards} - Your score: {user_score}")
print(f"Computer cards: {computer_cards[0]} - Computer score: {computer_score}")

if user_score==0 or computer_score==0 or user_score>21:
    game_over=True

