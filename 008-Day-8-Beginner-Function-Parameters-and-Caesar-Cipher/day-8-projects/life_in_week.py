# Life in Weeks


def life_in_weeks():
    while True:
        age = input("How old are you? ")
        if age.isdigit():
            age = int(age)
            if 0 <= age <= 90:
                break
            else:
                print("Sorry! Out of range!")
        else:
            print("Invalid input. Enter a number.")

    time_left = 90 - age
    weeks_left = round(time_left * 52.142857)  # weeks per year (52.142857 = 365 / 7)
    days_left = round(weeks_left * 7)
    hours_left = round(days_left * 24)
    print(
        f"You have {weeks_left} weeks left.\nThat's {days_left} Days.\nThats's {hours_left} Hours"
    )


life_in_weeks()
