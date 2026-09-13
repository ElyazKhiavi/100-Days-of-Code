import os
import requests
from dotenv import load_dotenv

load_dotenv()

FLIGHT_API_ENDPOINT = "https://app.100daysofpython.dev/v1/flights/search"


class FlightSearch:
    """Talks to the flight search API and returns raw JSON."""

    def __init__(self):
        self._flight_api_key = os.getenv("FLIGHT_API_KEY")

    def check_flights(
        self,
        origin_city_code,
        destination_city_code,
        from_time,
        to_time,
        nonstop_only=True,
    ):
        """
        Query the flight API for a round-trip search between two airports.

        nonstop_only=True  → only non-stop itineraries (adds `stops=1`).
        nonstop_only=False → any number of stops (omits `stops` entirely).

        Returns the parsed JSON on success, or None on any failure.
        """
        if not self._flight_api_key:
            print("There was a problem getting the flight api key from .env")
            return None

        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",  # 1 = round trip
            "adults": "1",
            "currency": "GBP",
            "api_key": self._flight_api_key,
        }

        # The API docs: `stops=1` means nonstop only. Omit the key for any stops.
        if nonstop_only:
            params["stops"] = "1"

        try:
            response = requests.get(url=FLIGHT_API_ENDPOINT, params=params)
            response.raise_for_status()
            data = response.json()

            # The course endpoint sometimes returns {"error": "..."} with a 200
            if "error" in data:
                print(f"API error: {data['error']}")
                return None

            return data

        except requests.exceptions.RequestException as e:
            print(f"Flight search request failed: {e}")
            return None
