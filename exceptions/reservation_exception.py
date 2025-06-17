# ---------------------------------------------------------------------
# EXCEPTION: ReservationError – Raised for reservation-related errors
# ---------------------------------------------------------------------
class ReservationError(Exception):
    def __init__(self, message):
        # Accepts a custom error message
        super().__init__(message)
