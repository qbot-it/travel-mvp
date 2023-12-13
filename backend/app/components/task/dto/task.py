from typing import Dict
from pydantic import BaseModel


class Task(BaseModel):
    id: str
    type: str
    result: Dict | None
    status: str


