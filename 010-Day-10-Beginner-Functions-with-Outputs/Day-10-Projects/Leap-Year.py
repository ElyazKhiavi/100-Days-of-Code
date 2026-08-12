# Leap Year


def main():
    while True:
        year = input("Enter a year to check: ")
        try:
            year = int(year)
            break
        except ValueError:
            print("Invalid! Please enter in a year.")

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(f"Year {year} is a Leap Year!")
                else:
                    print(f"Year {year} is NOT a Leap Year!")
            else:
                print(f"Year {year} is a Leap Year!")
        else:
            print(f"Year {year} is NOT a Leap Year!")


if __name__ == "__main__":
    main()
