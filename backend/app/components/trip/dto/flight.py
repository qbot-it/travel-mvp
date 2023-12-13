from pydantic import BaseModel


class Flight(BaseModel):
    title: str
    from_date: str
    to_date: str
    departure_date_time: str
    flight_code: str
    departure_airport_code: str
    destination_airport_code: str

    def to_json(self) -> dict:
        return {
            "title": self.title,
            "from_date": self.from_date,
            "to_date": self.to_date,
            "departure_date_time": self.departure_date_time,
            "flight_code": self.flight_code,
            "departure_airport_code": self.departure_airport_code,
            "destination_airport_code": self.destination_airport_code
        }


