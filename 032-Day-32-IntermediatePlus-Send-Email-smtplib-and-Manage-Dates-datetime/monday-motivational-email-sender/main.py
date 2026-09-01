# monday-motivational-email-sender

import os
import smtplib
import datetime as dt
from dotenv import load_dotenv
import random

load_dotenv()

SENDER = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER = os.getenv("RECEIVER_MAIL")

QUOTES = "./quotes.txt"


weekday = dt.datetime.now().weekday()


def get_quote():
    tab = str.maketrans("", "", "\\\n")
    try:
        with open(QUOTES, "r") as f:
            quotes = [quote.translate(tab) for quote in f.readlines()]
            return f"Subject:Weekly Motivation\n\n{random.choice(quotes)}"
    except FileNotFoundError:
        print("note found")
        return False


def main():
    if weekday == 0 and get_quote():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER, password=PASSWORD)
            connection.sendmail(from_addr=SENDER, to_addrs=RECEIVER, msg=get_quote)


if __name__ == "__main__":
    main()
