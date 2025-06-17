from models.library_item import LibraryItem
from models.reservable import Reservable

# ---------------------------------------------------------------------
# MAGAZINE CLASS – Inherits from both LibraryItem and Reservable
# ---------------------------------------------------------------------
class Magazine(LibraryItem):
    def __init__(self, item_id, title, author, issue):
        super().__init__(item_id, title, author)
        self.issue = issue  # Specific attribute for magazines

    def display_info(self):
        """
        Return a formatted string showing magazine details.
        Called when listing or searching for items.
        """
        return f"[Magazine] {self.title} Issue {self.issue} - Available: {self.available}"
    
    #------------------------------------------------------------------------
    # Uncomment the following method if magazines should support reservations
    # def reserve(self, user):
    #     """
    #     Mark this magazine as reserved by a user.
    #     Implements Reservable interface.
    #     """
    #     self.reserved_by = user