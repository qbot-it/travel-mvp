from pydantic import BaseModel
from .itinerary import Itinerary


class Flight(BaseModel):
    title: str
    price: float
    itineraries: list[Itinerary]

    def to_json(self) -> dict:
        return {
            "title": self.title,
            "price": self.price,
            "itineraries": list(map(lambda itinerary: itinerary.to_json(), self.itineraries))
        }

    @staticmethod
    def from_json(data: dict):
        return Flight(
            title=data['title'],
            price=data['price'],
            itineraries=list(map(lambda itinerary_data: Itinerary.from_json(itinerary_data), data['itineraries']))
        )
