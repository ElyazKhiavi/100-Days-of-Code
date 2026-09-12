from datetime import datetime, timedelta

from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager


def main():
    # Search window: tomorrow through ~6 months out
    from_time = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    to_time = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

    print(f"Flights From: {from_time} To: {to_time}")

    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    # 1. Get all rows from the sheet
    sheet_rows = data_manager.get_prices()
    if sheet_rows is None:
        print("There was an error getting the price data")
        return False

    # 2. For each row: query flights, find cheapest, compare, act
    for row in sheet_rows:
        origin_iata = row["originIata"]
        origin_city = row["originCity"]
        destination_iata = row["destinationIata"]
        destination_city = row["destinationCity"]
        lowest_price = row["lowestPrice"]
        row_id = row["id"]

        all_flight_data = flight_search.check_flights(
            origin_city_code=origin_iata,
            destination_city_code=destination_iata,
            from_time=from_time,
            to_time=to_time,
        )
        if all_flight_data is None:
            print(f"Could not fetch flights for {origin_city} → {destination_city}")
            continue  # try the next route instead of giving up entirely

        cheapest_flight = find_cheapest_flight(all_flight_data)

        print(
            f"Cheapest Flight from {origin_city}:{cheapest_flight.origin_airport} "
            f"to {destination_city}:{cheapest_flight.destination_airport} was "
            f"{cheapest_flight.price}£ ⏳ departure: {cheapest_flight.departure_time} "
            f"-> arrival: {cheapest_flight.arrival_time}"
        )

        # Skip the N/A placeholder and anything that isn't actually cheaper
        if cheapest_flight.price == "N/A":
            continue

        # Use float() so a decimal in the sheet doesn't crash the loop
        if float(cheapest_flight.price) < float(lowest_price):
            print(
                f"Found Lower Price For {origin_city}:{cheapest_flight.origin_airport} "
                f"to {destination_city}:{cheapest_flight.destination_airport}"
            )
            print(
                f"Previous Price was {lowest_price}£ new price is {cheapest_flight.price}£."
            )

            # Only email if the sheet was actually updated
            if data_manager.update_lowest_price(row_id, cheapest_flight.price):
                notification_manager.send_notification(
                    subject=(
                        f"Low price alert! "
                        f"{origin_city}:{cheapest_flight.origin_airport} to "
                        f"{destination_city}:{cheapest_flight.destination_airport}"
                    ),
                    body=(
                        f"Only {cheapest_flight.price}£.\n"
                        f"Fly from {origin_city}:{cheapest_flight.origin_airport} to "
                        f"{destination_city}:{cheapest_flight.destination_airport}\n"
                        f"Departure: {cheapest_flight.departure_time}"
                    ),
                )


if __name__ == "__main__":
    main()
