# ---------------------------------------------------------------------
# EXCEPTION: ItemNotAvailableError – Raised when an item is already borrowed
# ---------------------------------------------------------------------
class ItemNotAvailableError(Exception):
    def __init__(self, item_id):
        # Call the base class constructor with a custom message
        super().__init__(f"Item with ID {item_id} is not available.")


# ---------------------------------------------------------------------
# EXCEPTION: ItemNotFoundError – Raised when item ID is not found in the system
# ---------------------------------------------------------------------
class ItemNotFoundError(Exception):
    def __init__(self, item_id):
        # Custom error message for missing item
        super().__init__(f"Item with ID {item_id} was not found.")
