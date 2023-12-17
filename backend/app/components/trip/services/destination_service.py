from ..dto.destination import Destination


class DestinationService:

    def get_unique_destinations(self, destinations: list) -> list[Destination]:
        filtered = []

        for destination in destinations:
            if destination.airport_code not in filtered:
                filtered.append(destination)

        return filtered

