class InvalidObjectID(Exception):

    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


class EntityDoesNotExist(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


class InvalidEntity(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
