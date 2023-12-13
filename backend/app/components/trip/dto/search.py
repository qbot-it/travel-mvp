from typing import List
from pydantic import BaseModel


class Search(BaseModel):
    from_date: str | None
    to_date: str | None
    departure_airport_code: str | None
    location: List[float]

    def to_json(self) -> dict:
        return {
            "from_date": self.from_date,
            "to_date": self.to_date,
            "departure_airport_code": self.departure_airport_code,
            "location": self.location
        }

    @staticmethod
    def from_json(data):
        return Search(
            from_date=data['from_date'],
            to_date=data['to_date'],
            departure_airport_code=data['departure_airport_code'],
            location=data['location']
        )


