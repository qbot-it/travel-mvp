class Destination:
    name: str
    airport_code: str
    description: str

    def __init__(self, name: str, airport_code: str, description: str):
        self.name = name
        self.airport_code = airport_code
        self.description = description


