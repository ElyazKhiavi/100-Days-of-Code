import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_API_ENDPOINT = os.getenv("SHEETY_API_ENDPOINT")


class DataManager:
    """Handles reading and updating the Google Sheet via Sheety."""

    def __init__(self):
        self._authentication_token = os.getenv("SHEETY_AUTH_TOKEN")
        self.price_data = []

    def get_prices(self):
        """Return the sheet rows as a list of dicts, or None on failure."""
        if not all([self._authentication_token, SHEETY_API_ENDPOINT]):
            print("Auth token or API Endpoint missing in .env!")
            return None

        try:
            response = requests.get(
                url=SHEETY_API_ENDPOINT,
                headers={"Authorization": self._authentication_token},
            )
            response.raise_for_status()
            # .get() so a missing "prices" key doesn't raise KeyError
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
                headers={
                    "Authorization": self._authentication_token,
                    "Content-Type": "application/json",
                },
                json=new_data,
            )
            response.raise_for_status()
            print("New Price added to the spreadsheet")
            return True

        except requests.exceptions.RequestException as e:
            print(f"Data could not be updated, there was an error: {e}")
            return False
