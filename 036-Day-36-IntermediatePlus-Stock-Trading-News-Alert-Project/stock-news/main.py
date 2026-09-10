import os
import smtplib
from email.message import EmailMessage

import requests
from dotenv import load_dotenv

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------
STOCK = "META"
COMPANY_NAME = "Meta Platforms"

# Trigger thresholds: 2% up or down
INCREASE_PERCENT = 1.02
DECREASE_PERCENT = 0.98

load_dotenv()

"""
# .env.example  — copy to .env and fill in
ALPHAVANTAGE_API_KEY=
NEWS_API_KEY=
SMTP_SERVER=
SENDER_MAIL=
PASSWORD=
RECEIVER_MAIL=
"""

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
ALPHAVANTAGE_API = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY,
}

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API = "https://newsapi.org/v2/everything"

SENDER_MAIL = os.getenv("SENDER_MAIL")
RECEIVER_MAIL = os.getenv("RECEIVER_MAIL")
PASSWORD = os.getenv("PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")


# ------------------------------------------------------------
# Step 1: Check stock movement
# ------------------------------------------------------------
def check_stock():
    """
    Fetch the last two available trading days and check whether the closing
    price moved by more than the trigger thresholds.

    Returns a tuple:
        (buy, increase_percent, sell, decrease_percent, date_from, date_to)
    where date_from is the earlier date (YYYY-MM-DD) and date_to is the later one.
    Any percentage is None if that direction wasn't triggered.
    """
    response = requests.get(ALPHAVANTAGE_API, params=ALPHAVANTAGE_API_PARAMS)
    response.raise_for_status()
    data = response.json()

    # Guard against API limits / errors (Alpha Vantage returns "Note" or "Error Message")
    if "Time Series (Daily)" not in data:
        print(
            f"Alpha Vantage error: {data.get('Note') or data.get('Error Message') or 'Unknown'}"
        )
        return False, None, False, None, None, None

    series = data["Time Series (Daily)"]
    first_two = list(series.items())[:2]  # most recent first

    # first_two[1] = older day, first_two[0] = newer day
    date_from, data_from = first_two[1]
    date_to, data_to = first_two[0]

    close_from = float(data_from["4. close"])
    close_to = float(data_to["4. close"])

    buy = sell = False
    increase_percent = decrease_percent = None

    if close_from == 0:
        print("Stock closed at zero — cannot compute percentage change.")
        return False, None, False, None, date_from, date_to
    if close_to >= close_from * INCREASE_PERCENT:
        buy = True
        increase_percent = round((close_to - close_from) * 100 / close_from, 2)
    elif close_to <= close_from * DECREASE_PERCENT:
        sell = True
        decrease_percent = round((close_from - close_to) * 100 / close_from, 2)

    return buy, increase_percent, sell, decrease_percent, date_from, date_to


# ------------------------------------------------------------
# Step 2: Fetch news
# ------------------------------------------------------------
def get_news(date_from, date_to):
    """
    Fetch up to 3 recent news articles about the company.
    Returns a list of (title, description) tuples.
    """
    params = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "language": "en",
        "from": date_from,
        "to": date_to,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(NEWS_API, params=params)
    response.raise_for_status()
    articles = response.json().get("articles", [])

    # Take the first 3 (or fewer if not available)
    return [(a["title"], a["description"]) for a in articles[:3]]


# ------------------------------------------------------------
# Step 3: Send notification email
# ------------------------------------------------------------
def send_notif(subject, body):
    """Send an email using SMTP. Returns True on success, False otherwise."""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_MAIL
    msg["To"] = RECEIVER_MAIL
    msg.set_content(body)

    masked_recipient = (
        f"***@{RECEIVER_MAIL.split('@')[-1]}" if RECEIVER_MAIL else "unknown"
    )

    try:
        with smtplib.SMTP(SMTP_SERVER) as server:
            server.starttls()
            server.login(SENDER_MAIL, PASSWORD)
            refused = server.sendmail(
                from_addr=SENDER_MAIL,
                to_addrs=RECEIVER_MAIL,
                msg=msg.as_string(),
            )

        if refused:
            code, error = refused[RECEIVER_MAIL]
            print(
                f"⚠️  Mail refused for {masked_recipient} | Code: {code} | Reason: {error.decode()}"
            )
            return False

        print(f"✅ Email sent to {masked_recipient}")
        return True

    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Auth failed: {e.smtp_error.decode()}")
    except smtplib.SMTPRecipientsRefused as e:
        print(f"❌ Recipients refused: {e.recipients}")
    except smtplib.SMTPServerDisconnected as e:
        print(f"❌ Connection lost: {e}")
    except smtplib.SMTPException as e:
        print(f"❌ SMTP error: {type(e).__name__} - {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__} - {e}")

    return False


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
def main():
    buy, increase, sell, decrease, date_from, date_to = check_stock()

    # If the API failed or nothing triggered, bail out early
    if date_from is None:
        return

    if not (buy or sell):
        print("No significant movement today. No email sent.")
        return

    news = get_news(date_from, date_to)
    if not news:
        print("No news articles found.")
        return

    # Build the subject & body
    arrow = "🔺" if buy else "🔻"
    percent = increase if buy else decrease
    subject = f"{STOCK}: {arrow}{percent}%"

    body_lines = [subject]  # include the header line per spec
    for title, desc in news:
        body_lines.append(f"Headline: {title}")
        body_lines.append(f"Brief: {desc}\n")

    send_notif(subject, "\n".join(body_lines))


if __name__ == "__main__":
    main()
