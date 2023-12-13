from pydantic import BaseModel


class Payload(BaseModel):
    id: str
    is_refresh_token: bool
    exp: int

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "is_refresh_token": self.is_refresh_token,
            "exp": self.exp
        }

    @staticmethod
    def from_json(data: dict):
        return Payload(id=data['id'], is_refresh_token=data['is_refresh_token'], exp=data['exp'])
