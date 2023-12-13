from typing import List
from pydantic import BaseModel
from ...trip.dto.flight import Flight


class Result(BaseModel):
    trips: List[Flight]

    def to_json(self) -> dict:
        return {
            "trips": list(map(lambda flight: flight.to_json(), self.trips))
        }

    @staticmethod
    def from_json(data):
        return Result(
            trips=list(map(lambda trip: Flight(
                title=trip["title"],
                from_date=trip["from_date"],
                to_date=trip["to_date"],
                departure_date_time=trip["departure_date_time"],
                flight_code=trip["flight_code"],
                departure_airport_code=trip["departure_airport_code"],
                destination_airport_code=trip["destination_airport_code"]
            ), data['trips'])),
        )
