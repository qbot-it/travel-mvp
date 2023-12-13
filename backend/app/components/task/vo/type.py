from enum import Enum


class Type(Enum):
    UPLOAD = 'upload'
    SEARCH = 'search'

    def __str__(self) -> str:
        return self.value
