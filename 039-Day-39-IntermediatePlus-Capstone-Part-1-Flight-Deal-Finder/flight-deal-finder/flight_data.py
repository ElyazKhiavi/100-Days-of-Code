class FlightData:
    """Holds the fields we care about from a single flight itinerary."""

    def __init__(
        self,
        price,
        flight_number,
        origin_airport,
        destination_airport,
        departure_time,
        arrival_time,
    ):
        self.price = price
        self.flight_number = flight_number
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time


def find_cheapest_flight(data):
    """
    Pick the cheapest itinerary from the API response and return a FlightData object.
    If the response is empty or invalid, returns a FlightData where every field is "N/A".
    """
    if not data or not data.get("best_flights"):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    # best_flights is already sorted by relevance; we just want the cheapest
    flight_list = data["best_flights"]
    cheapest_flight = min(flight_list, key=lambda f: f["price"])

    price = cheapest_flight["price"]
    flight_number = cheapest_flight["flights"][0]["flight_number"]

    # An itinerary is a *list* of segments. If the flight has stops,
    # the first segment lands at the connection airport, not the destination.
    # So: departure info comes from the first segment, arrival info from the last.
    first_leg = cheapest_flight["flights"][0]
    last_leg = cheapest_flight["flights"][-1]

    origin_airport = first_leg["departure_airport"]["id"]
    departure_time = first_leg["departure_airport"]["time"]

    destination_airport = last_leg["arrival_airport"]["id"]
    arrival_time = last_leg["arrival_airport"]["time"]

    return FlightData(
        price,
        flight_number,
        origin_airport,
        destination_airport,
        departure_time,
        arrival_time,
    )

    