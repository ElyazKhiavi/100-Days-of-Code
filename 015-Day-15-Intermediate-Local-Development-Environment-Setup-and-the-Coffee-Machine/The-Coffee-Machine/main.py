# The Coffee Machine

DRINKS = {
    "1": {"name": "espresso", "water": 50, "coffee": 18, "milk": 0, "cost": 1.5},
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
        "cost": 3.00,
    },
}

INITIAL_MATERIALS = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
materials = INITIAL_MATERIALS.copy()


def menu():
    number = 0
    print()
    for i in DRINKS:
        number += 1
        print(f"{number}. {DRINKS[i]['name'].capitalize()} : ${DRINKS[i]['cost']}")
    user_input = input(f"What would you Like? 1-3: ")
    print()

    return user_input


def report():
    print("\n---Coffee Machine Report---")
    print(f"Water: {materials['water']}mL")
    print(f"Milk: {materials['milk']}mL")
    print(f"Coffee: {materials['coffee']}g")
    print(f"Money: ${materials['money']}")


def check_resources(drink):
    water_needed = DRINKS[drink]["water"]
    coffee_needed = DRINKS[drink]["coffee"]
    milk_needed = DRINKS[drink]["milk"]

    water_left = materials["water"]
    coffee_left = materials["coffee"]
    milk_left = materials["milk"]
    if water_left < water_needed:
        print("Sorry there is not enough water.")
        return False
    elif coffee_left < coffee_needed:
        print("Sorry there is not enough coffee.")
        return False
    elif milk_left < milk_needed:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True


def transaction(drink):
    cost = DRINKS[drink]["cost"]
    print(f"That will be ${cost}")
    while True:
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            if quarters < 0 or dimes < 0 or nickles < 0 or pennies < 0:
                print("Please entire in a positive number.")
            else:
                break
        except ValueError:
            print("INVALID! Please enter in a valid number.")
    coins_received = (
        (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    )
    if cost > coins_received:
        print(f"Sorry that's not enough money. Money refunded ${coins_received}.")
        return False
    elif cost == coins_received:
        print(f"That's on spot!! 🎯")
        return True
    else:
        print(f"Here is ${round((coins_received-cost),2)} in change.")
        return True


def make_coffee(drink):
    global materials

    drink = DRINKS[drink]

    materials["water"] -= drink["water"]
    materials["coffee"] -= drink["coffee"]
    materials["milk"] -= drink["milk"]
    materials["money"] += drink["cost"]


def run_coffee_machine():

    user_input = menu().lower().strip()

    if user_input == "off":
        return "OFF"
    elif user_input == "report":
        report()
        return "ON"
    else:
        if user_input in list(DRINKS.keys()):
            enough_resources = check_resources(user_input)
            if enough_resources:
                enough_money = transaction(user_input)
                if enough_money:
                    make_coffee(user_input)
                    print(f"Here is your {DRINKS[user_input]['name']} ☕ ENJOY!")
        else:
            print("INVALID! Try again.")
    return "ON"


print("Welcome to THE Coffee Machine!!!")


def main():
    state = "ON"
    while state != "OFF":
        state = run_coffee_machine()


if __name__ == "__main__":
    main()
