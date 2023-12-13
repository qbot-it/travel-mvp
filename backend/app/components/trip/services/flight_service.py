from ..dto.destination import Destination
from ..dto.flight import Flight
from ..dto.search import Search


class FlightService:

    def find_flights(self, search: Search, destination: Destination) -> list:
        flights = []

        # TODO: call flight API
        flights.append(Flight(
            title='test',
            from_date='test',
            to_date='test',
            departure_date_time='test',
            flight_code='test',
            departure_airport_code='test',
            destination_airport_code='test'
        ))

        return flights

    def get_unique_flights(self, flights: list) -> list:
        # TODO: return only unique flights
        return flights
