from datetime import datetime, timedelta

from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager


def build_email(origin_city, destination_city, flight, first_name, last_name):
    """Format the customer email body for a cheap-flight alert."""
    return (
        f"Hi {first_name} {last_name},\n\n"
        f"Great news — we just spotted a fare that matches your deal threshold.\n\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"  ROUTE      {origin_city} ({flight.origin_airport}) → "
        f"{destination_city} ({flight.destination_airport})\n"
        f"  PRICE      £{flight.price}\n"
        f"  STOPS      {flight.stops}\n"
        f"  DEPARTURE  {flight.departure_time}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"This price is below the lowest we've tracked for this route.\n"
        f"Deals like this don't usually stick around long — worth checking soon.\n\n"
        f"Safe travels,\n"
        f"Your Flight Deal Bot"
    )


def main():
    # Search window: tomorrow through ~6 months out
    from_time = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    to_time = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

    print(f"Flights From: {from_time} To: {to_time}")

    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    sheet_rows = data_manager.get_prices()
    if sheet_rows is None:
        print("There was an error getting the price data")
        return False
    # --- Fetch customers and send alerts ---
    user_emails = data_manager.get_user_emails()
    if user_emails is None:
        print("There was an error getting the customer list — no emails will be sent.")
        return False

    for row in sheet_rows:
        origin_iata = row["originIata"]
        origin_city = row["originCity"]
        destination_iata = row["destinationIata"]
        destination_city = row["destinationCity"]
        lowest_price = row["lowestPrice"]
        row_id = row["id"]

        # --- 1. Try a non-stop search first ---
        all_flight_data = flight_search.check_flights(
            origin_city_code=origin_iata,
            destination_city_code=destination_iata,
            from_time=from_time,
            to_time=to_time,
        )
        if all_flight_data is None:
            print(f"Could not fetch flights for {origin_city} → {destination_city}")
            continue

        cheapest_flight = find_cheapest_flight(all_flight_data)

        # --- 2. If nothing non-stop, retry allowing stops ---
        if cheapest_flight.price == "N/A":
            print(
                f"No direct flight to {destination_city}. Looking for indirect flights..."
            )
            indirect_flight_data = flight_search.check_flights(
                origin_city_code=origin_iata,
                destination_city_code=destination_iata,
                from_time=from_time,
                to_time=to_time,
                nonstop_only=False,
            )
            cheapest_indirect = find_cheapest_flight(indirect_flight_data)

            if cheapest_indirect.price == "N/A":
                # Nothing at all on this route — skip to the next row
                print(f"No flights found for {origin_city} → {destination_city}.")
                continue

            cheapest_flight = cheapest_indirect
            print("Cheapest indirect flight price is:")
        else:
            print("Cheapest flight price is:")

        print(
            f"{origin_city}:{cheapest_flight.origin_airport} "
            f"to {destination_city}:{cheapest_flight.destination_airport} was "
            f"{cheapest_flight.price}£ ⏳ departure: {cheapest_flight.departure_time} "
            f"-> arrival: {cheapest_flight.arrival_time}"
        )

        # --- 3. Compare with the sheet's lowest price ---
        if float(cheapest_flight.price) >= float(lowest_price):
            continue

        print(
            f"Found Lower Price For {origin_city}:{cheapest_flight.origin_airport} "
            f"to {destination_city}:{cheapest_flight.destination_airport}"
        )
        print(
            f"Previous Price was {lowest_price}£ new price is {cheapest_flight.price}£."
        )

        # --- 4. Update the sheet first; only email if the write succeeded ---
        if not data_manager.update_lowest_price(row_id, cheapest_flight.price):
            continue

        for user in user_emails:
            first_name = user["firstName"]
            last_name = user["lastName"]
            user_email = user["email"]

            notification_manager.send_notification(
                to_addr=user_email,
                subject=(
                    f"✈️ Good Deal Alert: {origin_city} → {destination_city} "
                    f"for only £{cheapest_flight.price}"
                ),
                body=build_email(
                    origin_city,
                    destination_city,
                    cheapest_flight,
                    first_name,
                    last_name,
                ),
            )


if __name__ == "__main__":
    main()
