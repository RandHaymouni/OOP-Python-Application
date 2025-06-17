from abc import ABC, abstractmethod

# ---------------------------------------------------------------------
# RESERVABLE INTERFACE – For items that support reservations
# ---------------------------------------------------------------------
class Reservable(ABC):
    @abstractmethod
    def reserve(self, user):
        """
        Abstract method to be implemented by any class that supports item reservation.
        'user' parameter represents the user who is reserving the item.
        """
        pass
