class ItemNotAvailableError(Exception):
    def __init__(self, message="Item is currently not available"):
        super().__init__(message)

class ItemNotFoundError(Exception):
    def __init__(self, message="Item not found in the system"):
        super().__init__(message)
