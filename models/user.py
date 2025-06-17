# ---------------------------------------------------------------------
# USER CLASS – Represents a library user
# ---------------------------------------------------------------------
class User:
    def __init__(self, user_id, name, email, borrowed_items=[]):
        self.user_id = user_id                
        self.name = name                      
        self.email = email                    
        self.borrowed_items = borrowed_items  

    def display_info(self):
        return f"User {self.name} ({self.email}) - ID: {self.user_id}"
