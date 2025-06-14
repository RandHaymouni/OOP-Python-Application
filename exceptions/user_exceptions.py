class UserNotFoundError(Exception):
    def __init__(self, message="User not found in the system"):
        super().__init__(message)