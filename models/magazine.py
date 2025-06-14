from models.library_item import LibraryItem
from models.reservable import Reservable

class Magazine(LibraryItem,Reservable):
    def __init__(self, item_id, title, author, issue_number, is_available=True):
        super().__init__(item_id, title, author, is_available)
        self.issue_number = issue_number

    def display_info(self):
        print(f"[Magazine] ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Issue: {self.issue_number}, Available: {self.is_available}")

    def reserve(self, user):
        if self.reserved_by:
            raise Exception("Magazine is already reserved.")
        self.reserved_by = user
    
    def to_dict(self):
        return {
            "type": "Magazine",
            "item_id": self.item_id,
            "title": self.title,
            "author": self.author,
            "issue_number": self.issue_number,
            "is_available": self.is_available
        }

    @staticmethod
    def from_dict(data):
        return Magazine(
            data['item_id'],
            data['title'],
            data['author'],
            data['issue_number'],
            data.get('is_available', True)
        )


