# practice project
# 🏦 Challenge: Simple Banking System

# Write a Python program that simulates a basic bank account. The user can check their balance, deposit money, withdraw money, or quit the program.


# 1. Starting Balance: $0.00- ✅
# 2. Menu Loop: The program repeatedly shows a menu until the user chooses to quit:✅
# 3. Deposit: User enters an amount. It must be positive. Add it to the balance and print a confirmation.
# 4. Withdraw: User enters an amount. It must be positive and not exceed the current balance. Deduct it and print a confirmation, or show an error message if the balance is insufficient.
# 5. Check Balance: Simply print the current balance.
# 6. Use Functions: Break the program into at least the following functions:
#     check_balance(balance) – displays the balance.
#     deposit(balance) – asks for amount, updates balance, returns the new balance.
#     withdraw(balance) – asks for amount, checks if possible, updates balance, returns the new balance.
#     main() – runs the menu loop and calls the other functions.
# 7. Variable Scope Practice: Try to pass the balance as an argument to each function and return the updated balance, rather than using a global variable. This is a great way to practice how data flows in and out of functions—a skill you’ll use constantly from now on.
def show_balance(balance):
    print(f"Current balance: ${balance:.2f}")


def deposit(balance):
    while True:
        amount = input("Enter deposit amount: ")
        if amount.isdigit():
            val = float(amount)
            balance += val
            print(f"Deposited ${val:.2f}. New balance: ${balance:.2f}")
            return balance
        print("You must enter a positive whole number!")


def withdraw(balance):
    if balance == 0:
        print("Your balance is $0.00. Nothing to withdraw.")
        return balance
    while True:
        amount = input("Enter withdrawal amount: ")
        if amount.isdigit():
            val = float(amount)
            if val > balance:
                print(f"Insufficient funds. Your balance is ${balance:.2f}")
                return balance  # or continue to ask again
            balance -= val
            print(f"Withdrew ${val:.2f}. New balance: ${balance:.2f}")
            return balance
        print("You must enter a positive whole number!")


def main():
    balance = 0.0
    while True:
        print("""
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Quit""")
        choice = input("Choose an option: ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid option. Please choose 1-4.")


main()
