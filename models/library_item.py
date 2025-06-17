from abc import ABC, abstractmethod

# ---------------------------------------------------------------------
# LIBRARYITEM CLASS (Abstract Base Class)
# Represents a generic item in the library
# ---------------------------------------------------------------------
class LibraryItem(ABC):
    def __init__(self, item_id, title, author):
        """
        Base constructor for any library item (e.g., book, DVD, magazine).
        Includes common properties: ID, title, author, availability, and reservation status.
        """
        self.item_id = item_id
        self.title = title
        self.author = author
        self.available = True          # Indicates if the item is available for borrowing
        self.reserved_by = None        # Stores the user who reserved the item (if any)

    @abstractmethod
    def display_info(self):
        pass

    def check_availability(self):
        """
        Check if the item is currently available.
        Returns True if available, False otherwise.
        """
        return self.available
