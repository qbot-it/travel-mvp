class DestinationService:

    def get_unique_destinations(self, destinations: list) -> list:
        filtered = []
        codes = {}

        for destination in destinations:
            if destination.airport_code not in codes:
                filtered.append(destination)

        return filtered

