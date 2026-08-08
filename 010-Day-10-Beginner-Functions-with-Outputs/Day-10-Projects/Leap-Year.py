# Leap Year

"""
If they are dividable by 4 they are leap years
    if they are dividable by 100
"""
# If English is not your first language, or if the above logic is confusing, try using this flow chart.
# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)
# Warning
# Your return should be a boolean and match the Example Output format exactly, including spelling and punctuation.
# Example Input 1
# 2400
# Example Return 1
# True
# Example Input 2
# 1989
# Example Return 2
# False


while True:
    while True:
        year = input("Enter a year to check: ")
        if year.isdigit():
            year = int(year)
            break

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