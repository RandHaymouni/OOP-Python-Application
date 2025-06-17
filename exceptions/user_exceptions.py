# ---------------------------------------------------------------------
# EXCEPTION: UserNotFoundError – Raised when a user ID is not found
# ---------------------------------------------------------------------
class UserNotFoundError(Exception):
    def __init__(self, user_id):
        # Call the base class constructor with a custom error message
        super().__init__(f"User with ID {user_id} was not found.")
