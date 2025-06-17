import json
import os
from models.book import Book
from models.magazine import Magazine
from models.dvd import DVD
from models.user import User
from exceptions.item_exceptions import *
from exceptions.user_exceptions import UserNotFoundError
from exceptions.reservation_exception import ReservationError


class Library:
    def __init__(self):
        # Dictionaries keyed by ID to store Item and User objects in memory
        self.items = {}
        self.users = {}

    # ---------------------------------------------------------------------
    # DATA LOADING / SAVING
    # ---------------------------------------------------------------------

    def load_data(self, items_file: str, users_file: str) -> None:
        """
        Read items and users from JSON files and rebuild the corresponding
        objects in memory.
        """
        try:
            # ---------- Load items ----------
            if os.path.exists(items_file):
                # Using `with open(...)` guarantees the file is closed automatically
                with open(items_file, 'r') as f:
                    items_data = json.load(f)

                for item in items_data:
                    # Select the class (Book / Magazine / DVD) based on the "type" field
                    cls = {'Book': Book, 'Magazine': Magazine, 'DVD': DVD}[item['type']]

                    # Instantiate the object by unpacking the stored dictionary
                    # cls(**item['data']) -> Book(**data) | Magazine(**data) | DVD(**data)
                    instance = cls(**item['data'])
                    instance.available = item['available']
                    self.items[instance.item_id] = instance
            else:
                print("Items file not found!")

            # ---------- Load users ----------
            if os.path.exists(users_file):
                with open(users_file, 'r') as f:
                    users_data = json.load(f)

                for user in users_data:
                    # Create a User object from the stored attributes
                    # User(**user) unpacks the dict directly into the constructor
                    instance = User(**user)
                    self.users[instance.user_id] = instance
            else:
                print("Users file not found!")

        except Exception as e:
            print("Error loading data:", e)

    def save_data(self, items_file: str, users_file: str) -> None:
        """
        Write the current in-memory data directly to disk,
        replacing any previous contents.
        """
        try:
            # ---------- Build fresh item/user structures ----------
            new_items_data = []
            for item in self.items.values():
                item_data = {
                    'item_id': item.item_id,
                    'title':   item.title,
                    'author':  item.author,
                }
                if isinstance(item, Book):
                    item_data['genre'] = item.genre
                elif isinstance(item, Magazine):
                    item_data['issue'] = item.issue
                elif isinstance(item, DVD):
                    item_data['duration'] = item.duration

                new_items_data.append({
                    'type': type(item).__name__,
                    'data': item_data,
                    'available': item.available
                })

            new_users_data = [{
                'user_id':        user.user_id,
                'name':           user.name,
                'email':          user.email,
                'borrowed_items': user.borrowed_items
            } for user in self.users.values()]

            # ---------- Persist to disk without merging ----------
            with open(items_file, 'w') as f:
                json.dump(new_items_data, f, indent=2)

            with open(users_file, 'w') as f:
                json.dump(new_users_data, f, indent=2)

        except Exception as e:
            print("Error saving data:", e)

    # ---------------------------------------------------------------------
    # CRUD OPERATIONS
    # ---------------------------------------------------------------------

    def add_user(self, user: User) -> None:
        """Insert a new User object into the in‑memory dictionary."""
        self.users[user.user_id] = user

    def add_item(self, item) -> None:
        """Insert a new Item object (Book / Magazine / DVD) into the library."""
        self.items[item.item_id] = item

    # -------------------- Circulation methods -----------------------------

    def borrow_item(self, user_id: str, item_id: str) -> None:
        if user_id not in self.users:
            raise UserNotFoundError(user_id)
        if item_id not in self.items:
            raise ItemNotFoundError(item_id)

        item = self.items[item_id]
        if not item.available:
            raise ItemNotAvailableError(item_id)

        item.available = False
        self.users[user_id].borrowed_items.append(item_id)

    def return_item(self, user_id: str, item_id: str) -> None:
        if user_id not in self.users:
            raise UserNotFoundError(user_id)
        if item_id not in self.items:
            raise ItemNotFoundError(item_id)

        self.items[item_id].available = True
        if item_id in self.users[user_id].borrowed_items:
            self.users[user_id].borrowed_items.remove(item_id)

    def reserve_item(self, user_id: str, item_id: str) -> None:
        if user_id not in self.users:
            raise UserNotFoundError(user_id)
        if item_id not in self.items:
            raise ItemNotFoundError(item_id)

        item = self.items[item_id]
        if not hasattr(item, 'reserve'):
            raise ReservationError("Item does not support reservation.")
        if item.reserved_by:
            raise ReservationError("Item already reserved.")

        item.reserve(user_id)

    # ---------------------------------------------------------------------
    # INFORMATION QUERIES
    # ---------------------------------------------------------------------

    def search_items(self, keyword: str):
        """Return display info for items whose title contains the keyword."""
        return [
            item.display_info()
            for item in self.items.values()
            if keyword.lower() in item.title.lower()
        ]

    def get_all_items(self):
        """Return display info for all items in the library."""
        return [item.display_info() for item in self.items.values()]
