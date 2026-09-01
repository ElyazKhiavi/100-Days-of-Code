import os
import smtplib
import csv
from datetime import date
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
SENDER = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASSWORD")
PROVIDER_SMTP = "smtp.gmail.com"
RECEIVER = os.getenv("RECEIVER_MAIL")  # Not used in this script, kept for reference

MSG_FILE = "./message.txt"
BIRTHDAYS_CSV = "./birthdays.csv"

# Today's date in month-day format (e.g., "12-25")
today = date.today()
today_str = f"{today.month}-{today.day}"


def read_birthdays():
    """
    Read birthdays.csv and return a list of dictionaries.
    Each dictionary has keys: name, email, month, day.
    Returns empty list if file not found or invalid.
    """
    try:
        with open(BIRTHDAYS_CSV, "r") as f:
            reader = csv.DictReader(f)
            # Convert month/day to int for reliable comparison
            birthdays = []
            for row in reader:
                birthdays.append(
                    {
                        "name": row["name"],
                        "email": row["email"],
                        "month": int(row["month"]),
                        "day": int(row["day"]),
                    }
                )
            return birthdays
    except FileNotFoundError:
        print(f"Error: {BIRTHDAYS_CSV} not found.")
        return []
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []


def create_message(name):
    """
    Read the message template and replace [Name] with the recipient's name.
    Returns the full email message (subject + body).
    """
    try:
        with open(MSG_FILE, "r") as f:
            template = f.read().strip()
            message_body = template.replace("[Name]", name)
            # Add subject header
            full_message = f"Subject: Happy Birthday!\n\n{message_body}"
            return full_message
    except FileNotFoundError:
        print(f"Error: {MSG_FILE} not found.")
        return None
    except Exception as e:
        print(f"Error reading message file: {e}")
        return None


def send_email(to_address, message):
    """
    Send an email via Gmail SMTP.
    Returns True on success, False on failure.
    """
    if not SENDER or not PASSWORD:
        print("Error: Email credentials not set in .env")
        return False

    try:
        with smtplib.SMTP(PROVIDER_SMTP) as connection:
            connection.starttls()
            connection.login(user=SENDER, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER,
                to_addrs=to_address,
                msg=message,
            )
        return True
    except smtplib.SMTPAuthenticationError:
        print(f"Authentication failed for {SENDER}. Check your app password.")
        return False
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")
        return False


def main():
    """Main routine: find today's birthdays and send emails."""
    birthdays = read_birthdays()
    if not birthdays:
        print("No birthday data loaded.")
        return

    # Find all people whose birthday is today
    today_birthdays = [b for b in birthdays if f"{b['month']}-{b['day']}" == today_str]

    if not today_birthdays:
        print("No birthdays today.")
        return

    for person in today_birthdays:
        name = person["name"]
        email = person["email"]
        message = create_message(name)
        if message is None:
            print("Message template missing. Aborting sending.")
            return  # stop everything

        if send_email(email, message):
            print(f"Birthday email sent to {name} ({email})")
        else:
            print(f"Failed to send email to {name}")

    print("Finished processing today's birthdays.")


if __name__ == "__main__":
    main()
