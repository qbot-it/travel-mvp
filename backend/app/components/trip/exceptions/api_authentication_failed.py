class ApiAuthenticationFailedException(Exception):
    message = "API authentication failed"

    def __init__(self, message: str | None = None):
        if isinstance(message, str):
            self.message += f"{self.message}: {message}"
