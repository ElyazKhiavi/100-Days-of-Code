# Coffee Machine
# --------------
# This program simulates a simple coffee machine.
# The user can choose a drink, insert coins, and receive change.
# The machine tracks resources and money earned.

# Drinks available, each with required resources and cost.
DRINKS = {
    "1": {
        "name": "espresso",
        "water": 50,  # ml
        "coffee": 18,  # g
        "milk": 0,  # ml
        "cost": 1.5,  # $
    },
    "2": {
        "name": "latte",
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "cost": 2.5,
    },
    "3": {
        "name": "cappuccino",
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "cost": 3.0,
    },
}

# Starting resources (water, milk, coffee, money)
INITIAL_MATERIALS = {
    "water": 300,  # ml
    "milk": 200,  # ml
    "coffee": 100,  # g
    "money": 0,  # $
}

# Current resources (copy so INITIAL_MATERIALS stays unchanged if we ever need to reset)
materials = INITIAL_MATERIALS.copy()

# Coin values in dollars
PENNY_VALUE = 0.01
NICKEL_VALUE = 0.05
DIME_VALUE = 0.10
QUARTER_VALUE = 0.25


def menu():
    """
    Show the drink menu and ask the user to choose.
    Returns the user's input as a string (not lower-cased here; we do that later).
    """
    print("\n--- Menu ---")
    for key in DRINKS:
        drink = DRINKS[key]
        print(f"{key}. {drink['name'].capitalize()} : ${drink['cost']:.2f}")
    user_input = input("What would you like? (1-3): ").strip().lower()
    return user_input


def report():
    """Print the current resource levels and money earned."""
    print("\n--- Coffee Machine Report ---")
    print(f"Water: {materials['water']} ml")
    print(f"Milk: {materials['milk']} ml")
    print(f"Coffee: {materials['coffee']} g")
    print(f"Money: ${materials['money']:.2f}")


def check_resources(drink_choice):
    """
    Check if there are enough resources to make the chosen drink.
    Returns True if sufficient, False otherwise (and prints what's missing).
    """
    drink = DRINKS[drink_choice]
    water_needed = drink["water"]
    coffee_needed = drink["coffee"]
    milk_needed = drink["milk"]

    # Check each resource; if any is insufficient, print a message and stop.
    if materials["water"] < water_needed:
        print("Sorry, there is not enough water.")
        return False
    if materials["coffee"] < coffee_needed:
        print("Sorry, there is not enough coffee.")
        return False
    if materials["milk"] < milk_needed:
        print("Sorry, there is not enough milk.")
        return False

    # All resources are sufficient
    return True


def get_coin_input(coin_name, coin_value):
    """
    Ask the user how many of a particular coin they want to insert.
    Keeps asking until a non-negative integer is entered.
    Returns the total value of those coins.
    """
    while True:
        try:
            count = int(input(f"How many {coin_name}?: "))
            if count < 0:
                print("Please enter a non-negative number.")
                continue
            return count * coin_value
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def transaction(drink_choice):
    """
    Handle the payment process.
    Returns True if payment is successful, False if insufficient money.
    """
    drink = DRINKS[drink_choice]
    cost = drink["cost"]
    print(f"\nThat will be ${cost:.2f}")

    # Ask for coins and calculate total inserted money
    total_money = 0
    total_money += get_coin_input("quarters", QUARTER_VALUE)
    total_money += get_coin_input("dimes", DIME_VALUE)
    total_money += get_coin_input("nickles", NICKEL_VALUE)
    total_money += get_coin_input("pennies", PENNY_VALUE)

    # Check if enough money was inserted
    if total_money < cost:
        print(f"Sorry, that's not enough money. Money refunded: ${total_money:.2f}")
        return False
    elif total_money == cost:
        print("Exact amount received. No change needed.")
        return True
    else:
        change = round(total_money - cost, 2)  # round to avoid floating point errors
        print(f"Here is ${change:.2f} in change.")
        return True


def make_coffee(drink_choice):
    """
    Deduct the required resources and add the cost to the machine's money.
    Assumes check_resources() was already called and returned True.
    """
    drink = DRINKS[drink_choice]

    # Subtract resources
    materials["water"] -= drink["water"]
    materials["coffee"] -= drink["coffee"]
    materials["milk"] -= drink["milk"]

    # Add money from the drink
    materials["money"] += drink["cost"]


def run_coffee_machine():
    """
    Execute one cycle of the coffee machine:
    - Show menu, get user choice.
    - Handle special commands ("off", "report").
    - If a drink is chosen, check resources -> process payment -> make coffee.
    Returns "OFF" if the machine should shut down, otherwise "ON".
    """
    user_input = menu().lower()  # lower-case so "OFF", "Off", etc. all work

    if user_input == "off":
        return "OFF"
    elif user_input == "report":
        report()
        return "ON"
    elif user_input in DRINKS:  # user entered 1, 2, or 3
        if check_resources(user_input):
            if transaction(user_input):
                make_coffee(user_input)
                drink_name = DRINKS[user_input]["name"]
                print(f"Here is your {drink_name} ☕ Enjoy!")
        # If resources insufficient or payment failed, we simply return to the menu
        # (nothing more to do, the appropriate error messages have been printed)
        return "ON"
    else:
        print("Invalid choice. Please try again.")
        return "ON"


def main():
    """Main program loop."""
    print("Welcome to the Coffee Machine!")

    state = "ON"
    while state != "OFF":
        state = run_coffee_machine()


if __name__ == "__main__":
    main()
