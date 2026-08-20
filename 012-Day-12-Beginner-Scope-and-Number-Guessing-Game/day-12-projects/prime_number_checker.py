"""
Prime Number Checker
--------------------
This program checks whether a user-provided number is a prime number.
A prime number is only divisible by 1 and itself.

Note: 2 is prime, 1 is not prime (by definition).
"""


def get_positive_integer():
    """
    Repeatedly ask the user for a whole number >= 1.
    Returns the number as an int.
    """
    while True:
        user_input = input("Enter a positive whole number: ").strip()
        try:
            number = int(user_input)
            if number < 1:
                print(
                    "Prime numbers are defined for positive integers only. Try again."
                )
                continue
            return number
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")


def is_prime(num):
    """
    Check if a number is prime.
    Returns True if prime, False otherwise.
    """
    # 1 is not a prime number by definition
    if num == 1:
        return False

    # 2 is the only even prime number
    if num == 2:
        return True

    # Any other even number cannot be prime
    if num % 2 == 0:
        return False

    # Check divisibility by odd numbers from 3 up to num-1.
    # (A more efficient method would be to check up to sqrt(num),
    #  but this is kept simple for a beginner project.)
    for divisor in range(3, num, 2):  # step by 2 to skip evens
        if num % divisor == 0:
            return False

    # If no divisor was found, it's prime
    return True


def main():
    """Main loop: ask for a number, display result, offer to repeat."""
    while True:
        number = get_positive_integer()
        prime_status = is_prime(number)

        if prime_status:
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

        again = input("\nCheck another number? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


# Run the program
if __name__ == "__main__":
    main()
