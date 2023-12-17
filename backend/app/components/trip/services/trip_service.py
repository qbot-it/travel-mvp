from ..services.recommender.destination_recommender import DestinationRecommender
from .destination_service import DestinationService
from ..services.flights.flight_service import FlightService
from .image_selection_service import ImageSelectionService
from ..dto.flight.flight import Flight
from ..dto.search import Search
from ...image.dto.descriptor import Descriptor
from ...user.models.user import User


class TripService:
    __image_selection_service: ImageSelectionService
    __destination_service: DestinationService
    __recommender: DestinationRecommender
    __flight_service: FlightService

    def __init__(self):
        self.__image_selection_service = ImageSelectionService()
        self.__flight_service = FlightService()
        self.__destination_service = DestinationService()
        self.__recommender = DestinationRecommender()

    def find_trips(self, user: User, search: Search) -> list[Flight]:
        images = self.__image_selection_service.get_relevant_images(user)

        image_descriptions = []
        for image in images:
            descriptor = Descriptor.from_json(image.descriptor)
            image_descriptions.append(descriptor.text)

        destinations = []
        if len(image_descriptions) > 0:
            destinations = self.__recommender.run(image_descriptions)
            destinations = self.__destination_service.get_unique_destinations(destinations)

        flights = []
        for destination in destinations:
            destination_flights = self.__flight_service.find_flights(search, destination)
            flights.extend(destination_flights)

        return flights
