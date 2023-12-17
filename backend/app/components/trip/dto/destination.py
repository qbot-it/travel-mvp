class Destination:
    name: str
    airport_code: str
    description: str | None

    def __init__(self, name: str, airport_code: str, description: str | None = None):
        self.name = name
        self.airport_code = airport_code
        self.description = description


