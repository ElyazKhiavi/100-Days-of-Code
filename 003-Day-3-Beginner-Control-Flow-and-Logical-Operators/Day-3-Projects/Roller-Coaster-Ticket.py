print("Welcome to the Memory Train!")
print("Please get your Tickets first: ")

height = float(input("How tall are you in cm? "))
cost = 0
if height > 120:
    can_ride = True
    age = int(input("How old are you? "))
    if age <= 12:
        cost = 5
    elif 12 < age <= 18:
        cost = 7
    elif 18 < age <= 45:
        cost = 12
    elif 45 < age <= 55:
        cost = 0
    else:
        can_ride = False
        print("Sorry You're too old!, Can't ride!")

    if can_ride == True:
        ride = input(
            "Okay You're looking good,\nWill you want photos after your ride? (yes or no) "
        )
        if ride[0].lower() == "y":
            cost += 3
            print("Excellent!")
            print(f"Your ticket will be ${cost}")
        else:
            if cost == 0:
                print("Congratulations, You get a free Ride!")
            else:
                print(f"Your ticket will be ${cost}")
else:
    print("Sorry you're too short!, Can't ride!")
