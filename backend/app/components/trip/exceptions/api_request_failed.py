class ApiRequestFailedException(Exception):
    message = "API request failed"

    def __init__(self, message: str | None = None):
        if isinstance(message, str):
            self.message += f"{self.message}: {message}"
