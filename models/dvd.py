from models.library_item import LibraryItem
from models.reservable import Reservable

# ---------------------------------------------------------------------
# DVD CLASS – Inherits from both LibraryItem and Reservable
# ---------------------------------------------------------------------
class DVD(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, duration):
        """
        Initialize a DVD object with ID, title, author, and duration.
        Inherits common item attributes from LibraryItem.
        """
        super().__init__(item_id, title, author)
        self.duration = duration  # DVD-specific attribute

    def display_info(self):
        """
        Return a formatted string showing DVD details.
        Called when listing or searching for items.
        """
        return f"[DVD] {self.title} by {self.author} - Duration: {self.duration} - Available: {self.available}"

    def reserve(self, user):
        """
        Mark this DVD as reserved by a user.
        Implements Reservable interface.
        """
        self.reserved_by = user
