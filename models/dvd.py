from models.library_item import LibraryItem
from models.reservable import Reservable

class DVD(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, duration, is_available=True):
        super().__init__(item_id, title, author, is_available)
        self.duration = duration
        self.reserved_by = None

    def display_info(self):
        print(f"[DVD] ID: {self.item_id}, Title: {self.title}, Director: {self.author}, Duration: {self.duration} mins, Available: {self.is_available}")

    def reserve(self, user):
        if self.reserved_by:
            raise Exception("DVD is already reserved.")
        self.reserved_by = user

    def to_dict(self):
        return {
            "type": "DVD",
            "item_id": self.item_id,
            "title": self.title,
            "author": self.author,
            "duration": self.duration,
            "is_available": self.is_available
        }

    @staticmethod
    def from_dict(data):
        return DVD(
            data['item_id'],
            data['title'],
            data['author'],
            data['duration'],
            data.get('is_available', True)
        )
