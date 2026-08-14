from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Recreate the coffee machine program but this time with OOP approach


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def start_coffee_machine():
    order = input(f"What would you like? {menu.get_items()}: ")
    if order == "off":
        return "OFF"
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
        return "ON"
    elif menu.find_drink(order):
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        return "ON"


def main():
    state = "ON"
    while state != "OFF":
        state = start_coffee_machine()


if __name__ == "__main__":
    main()
