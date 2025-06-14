from models.library_item import LibraryItem
from models.reservable import Reservable

class Book(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, genre, is_available=True):
        super().__init__(item_id, title, author, is_available)
        self.genre = genre
        self.reserved_by = None

    def display_info(self):
        print(f"[Book] ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Available: {self.is_available}")

    def reserve(self, user):
        if self.reserved_by:
            raise Exception("Book is already reserved.")
        self.reserved_by = user

    def to_dict(self):
        return {
            "type": "Book",
            "item_id": self.item_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "is_available": self.is_available
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data['item_id'],
            data['title'],
            data['author'],
            data['genre'],
            data.get('is_available', True)
        )

