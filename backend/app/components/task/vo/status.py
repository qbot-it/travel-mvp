from enum import Enum


class Status(str, Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    FINISHED = 'finished'

    def __str__(self) -> str:
        return self.value
