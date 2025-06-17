import uuid
from models.library import Library
from models.user import User

# ---------------------------------------------------------------------
# APPLICATION CLASS
# ---------------------------------------------------------------------
class LibraryApp:
    def __init__(self):
        """Create a Library instance and load data from JSON files."""
        self.library = Library()
        self.library.load_data("data/items.json", "data/users.json")

    # -----------------------------------------------------------------
    # USER INTERFACE
    # -----------------------------------------------------------------
    def display_menu(self) -> None:
        """Print the main menu that drives user interaction."""
        print("""
                Welcome to the Library System
                1. View all available items
                2. Search item by title or type
                3. Register as a new user
                4. Add new item
                5. Borrow an item
                6. Reserve an item
                7. Return an item
                8. Delete an item
                9. Delete a user
                10. Exit and Save
                """)

    # -----------------------------------------------------------------
    # MAIN LOOP
    # -----------------------------------------------------------------
    def run(self) -> None:
        """Continuously prompt the user until they choose to exit."""
        while True:
            self.display_menu()
            try:
                choice = input("Enter choice: ")

                # ------------------ READ‑ONLY QUERIES -------------------
                if choice == '1':
                    # Display every item currently stored in memory
                    for info in self.library.get_all_items():
                        print(info)

                elif choice == '2':
                    # Search items by keyword contained in the title
                    keyword = input("Enter keyword OR title to search: ")
                    for info in self.library.search_items(keyword):
                        print(info)

                # ------------------ USER MANAGEMENT ---------------------
                elif choice == '3':
                    print("Add New User")
                    name  = input("Enter your name: ")
                    email = input("Enter your email: ")
                    user_id = str(uuid.uuid4())        # Generate unique ID
                    user = User(user_id, name, email)
                    self.library.add_user(user)
                    print(f"User registered with ID: {user_id}")

                # ------------------ ITEM MANAGEMENT ---------------------
                elif choice == '4':
                    print("Add New Item")
                    item_type = input("Enter item type (Book, Magazine, DVD): ").strip()
                    item_id   = str(uuid.uuid4())
                    title     = input("Enter title: ").strip()
                    author    = input("Enter author: ").strip()

                    # Instantiate the correct subclass based on user choice
                    if item_type.lower() == "book":
                        genre = input("Enter genre: ").strip()
                        from models.book import Book
                        new_item = Book(item_id, title, author, genre)
                    elif item_type.lower() == "magazine":
                        issue = input("Enter issue: ").strip()
                        from models.magazine import Magazine
                        new_item = Magazine(item_id, title, author, issue)
                    elif item_type.lower() == "dvd":
                        duration = input("Enter duration: ").strip()
                        from models.dvd import DVD
                        new_item = DVD(item_id, title, author, duration)
                    else:
                        print("Invalid item type.")
                        continue  

                    new_item.available = True     
                    self.library.add_item(new_item)
                    print(f"{item_type} added successfully with ID: {item_id}")

                # ------------------ CIRCULATION -------------------------
                elif choice == '5':
                    user_id = input("Enter user ID: ")
                    item_id = input("Enter item ID to borrow: ")
                    self.library.borrow_item(user_id, item_id)
                    print("Item borrowed successfully.")

                elif choice == '6':
                    user_id = input("Enter user ID: ")
                    item_id = input("Enter item ID to reserve: ")
                    self.library.reserve_item(user_id, item_id)
                    print("Item reserved successfully.")

                elif choice == '7':
                    user_id = input("Enter user ID: ")
                    item_id = input("Enter item ID to return: ")
                    self.library.return_item(user_id, item_id)
                    print("Item returned successfully.")

                # ------------------ DELETE OPERATIONS -------------------
                elif choice == '8':
                    item_id = input("Enter item ID to delete: ").strip()
                    if item_id in self.library.items:
                        del self.library.items[item_id]
                        print(f"Item {item_id} deleted successfully.")
                    else:
                        print("Item ID not found.")

                elif choice == '9':
                    user_id = input("Enter user ID to delete: ").strip()
                    if user_id in self.library.users:
                        del self.library.users[user_id]
                        print(f"User {user_id} deleted successfully.")
                    else:
                        print("User ID not found.")

                # ------------------ EXIT & PERSIST ----------------------
                elif choice == '10':
                    self.library.save_data("data/items.json", "data/users.json")
                    print("Library data saved. Exiting.")
                    break

                else:
                    print("Invalid choice. Try again.")

            # --------------- ERROR HANDLING & LOOP SEPARATOR ------------
            except Exception as e:
                print("Error:", e)
            finally:
                print("--------------------------")

# ---------------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------------
if __name__ == "__main__":
    app = LibraryApp()
    app.run()
