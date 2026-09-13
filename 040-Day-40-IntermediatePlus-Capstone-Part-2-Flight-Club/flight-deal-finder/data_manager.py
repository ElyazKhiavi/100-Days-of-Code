import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_API_ENDPOINT = os.getenv("SHEETY_API_ENDPOINT")
SHEETY_EMAILS_API_ENDPOINT = os.getenv("SHEETY_EMAILS_API_ENDPOINT")
AUTH_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")


class DataManager:
    """Handles reading and updating the Google Sheet via Sheety."""

    def __init__(self):
        self._headers = {
            "Authorization": AUTH_TOKEN,
            "Content-Type": "application/json",
        }
        self.price_data = []

    def get_prices(self):
        """Return the price rows as a list of dicts, or None on failure."""
        # Only validate the vars THIS method actually uses.
        if not all([AUTH_TOKEN, SHEETY_API_ENDPOINT]):
            print("Auth token or price endpoint missing in .env!")
            return None

        try:
            response = requests.get(
                url=SHEETY_API_ENDPOINT,
                headers=self._headers,
            )
            response.raise_for_status()
            self.price_data = response.json().get("prices", [])
            return self.price_data

        except requests.exceptions.RequestException as e:
            print(f"Requests Error: {e}")
            return None

    def update_lowest_price(self, row_id, lowest_price):
        """
        Update the 'lowestPrice' cell for a given sheet row.
        Returns True on success, False otherwise.
        """
        new_data = {"price": {"lowestPrice": lowest_price}}

        try:
            response = requests.put(
                url=f"{SHEETY_API_ENDPOINT}/{row_id}",
                headers=self._headers,
                json=new_data,
            )
            response.raise_for_status()
            print("New Price added to the spreadsheet")
            return True

        except requests.exceptions.RequestException as e:
            print(f"Data could not be updated, there was an error: {e}")
            return False

    def get_user_emails(self):
        """
        Return the list of customer rows from the Google Form sheet,
        or None on failure.
        """
        if not all([AUTH_TOKEN, SHEETY_EMAILS_API_ENDPOINT]):
            print("Auth token or emails endpoint missing in .env!")
            return None

        try:
            response = requests.get(
                url=SHEETY_EMAILS_API_ENDPOINT, headers=self._headers
            )
            response.raise_for_status()
            return response.json().get("users", [])

        except requests.exceptions.RequestException as e:
            print(f"Requests Error: {e}")
            return None
