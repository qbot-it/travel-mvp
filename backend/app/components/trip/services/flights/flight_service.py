from ...dto.destination import Destination
from ...dto.flight.flight import Flight
from ...dto.search import Search
from ...services.flights.amadeus_api_service import AmadeusApiService


class FlightService:
    __amadeus_api_service: AmadeusApiService

    def __init__(self):
        self.__amadeus_api_service = AmadeusApiService()

    def find_flights(self, search: Search, destination: Destination) -> list[Flight]:
        return self.__amadeus_api_service.get_flight_offers(
            name=destination.name,
            origin=search.departure_airport_code,
            destination=destination.airport_code,
            departure_date=search.from_date,
            adults=1,
            return_date=search.to_date,
        )
