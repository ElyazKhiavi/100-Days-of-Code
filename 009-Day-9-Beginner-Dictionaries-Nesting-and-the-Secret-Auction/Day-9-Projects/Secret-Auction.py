# Secret Auction
import os



def submit_action(bidders):
    user_name = input("What is your name? ")
    while True:
        user_bid = input("How much is your bid? $")
        if user_bid.isdigit():
            user_bid = int(user_bid)
            break
        else:
            print("You must enter in a Number! ")
    bidders[user_name] = user_bid


def auction_winner(bidders):
    # highest = 0
    # for i in b:
    #     if b[i] > highest:
    #         highest=b[i]
    #         winner = i
    ### There i cooler way of doing this dictionary value comparing
    winner = max(bidders, key=bidders.get)
    print(f"Okay, the grand winner of the bid is {winner} with ${bidders[winner]}!")


print("Welcome to the auction! Thank you for joining us today.")


def main():
    while True:
        bidders = {}
        while True:
            submit_action(bidders)
            other_bidders = input("Are there any other bidders? y/n: ").lower()
            if other_bidders != "y":
                os.system("clear")
                auction_winner(bidders)
                break
            os.system("clear")
        re_enter = input("Are you interested in other items? y/n: ").lower()
        if re_enter != "y":
            print("Thank you for participating! Have a great day. Goodbye!")
            break
        os.system("clear")
        print("Great! Let's move on to the next item.")


main()
