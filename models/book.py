from models.library_item import LibraryItem
from models.reservable import Reservable

# ---------------------------------------------------------------------
# BOOK CLASS – Inherits from both LibraryItem and Reservable
# ---------------------------------------------------------------------
class Book(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, genre):
        super().__init__(item_id, title, author)
        self.genre = genre  # Book-specific attribute

    def display_info(self):
        return f"[Book] {self.title} by {self.author} - Genre: {self.genre} - Available: {self.available}"

    def reserve(self, user):
        """
        Mark this book as reserved by a user.
        Implements Reservable interface.
        """
        self.reserved_by = user
