from pydantic import BaseModel


class Segment(BaseModel):
    departure_airport_code: str
    departure_date_time: str
    arrival_airport_code: str
    arrival_date_time: str
    aircraft_code: str
    carrier_code: str
    number: str

    def to_json(self) -> dict:
        return {
            "departure_airport_code": self.departure_airport_code,
            "departure_date_time": self.departure_date_time,
            "arrival_airport_code": self.arrival_airport_code,
            "arrival_date_time": self.arrival_date_time,
            "aircraft_code": self.aircraft_code,
            "carrier_code": self.carrier_code,
            "number": self.number,
        }

    @staticmethod
    def from_json(data: dict):
        return Segment(
            departure_airport_code=data['departure_airport_code'],
            departure_date_time=data['departure_date_time'],
            arrival_airport_code=data['arrival_airport_code'],
            arrival_date_time=data['arrival_date_time'],
            aircraft_code=data['aircraft_code'],
            carrier_code=data['carrier_code'],
            number=data['number'],
        )
