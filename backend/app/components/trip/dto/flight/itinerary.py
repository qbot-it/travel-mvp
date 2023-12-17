from pydantic import BaseModel
from .segment import Segment


class Itinerary(BaseModel):
    segments: list[Segment]

    def to_json(self) -> dict:
        return {
            "segments": list(map(lambda segment: segment.to_json(), self.segments))
        }

    @staticmethod
    def from_json(data: dict):
        return Itinerary(
            segments=list(map(lambda segment_data: Segment.from_json(segment_data), data['segments']))
        )
