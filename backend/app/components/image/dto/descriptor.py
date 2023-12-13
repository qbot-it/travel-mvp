class Descriptor:

    def __init__(self, text: str, vector: list):
        self.vector = vector
        self.text = text

    text: str
    vector: list

    def to_json(self) -> dict:
        return {
            "text": self.text,
            "vector": self.vector
        }

    @staticmethod
    def from_json(data: dict):
        return Descriptor(data['text'], data['vector'])
