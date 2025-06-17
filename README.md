# 📚 Library Management System

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)

A comprehensive Python-based Library Management System that enables efficient management of books, magazines, and DVDs. The system supports user registration, item borrowing/returning, reservations, and persistent data storage through JSON files.

## ✨ Features

- 📖 **Multi-format Support**: Manage Books, Magazines, and DVDs
- 👥 **User Management**: Register and manage library users
- 🔍 **Smart Search**: Search items by title or type keywords
- 📋 **Borrowing System**: Complete borrow and return functionality
- 🔖 **Reservation System**: Reserve items that support reservations
- 💾 **Data Persistence**: Automatic save/load using JSON files
- ⚠️ **Error Handling**: Comprehensive exception handling
- 🖥️ **CLI Interface**: User-friendly command-line interface

## 🏗️ Project Structure

```
library-management-system/
│
├── models/
│   ├── book.py              # Book class (LibraryItem + Reservable)
│   ├── dvd.py               # DVD class (LibraryItem + Reservable)
│   ├── magazine.py          # Magazine class (LibraryItem only)
│   ├── library.py           # Core Library management class
│   ├── user.py              # User class definition
│   └── reservable.py        # Abstract Reservable interface
│
├── exceptions/
│   ├── item_exceptions.py   # Item-related exceptions
│   ├── user_exceptions.py   # User-related exceptions
│   └── reservation_exception.py # Reservation exceptions
│
├── data/
│   ├── items.json          # Persistent item storage
│   └── users.json          # Persistent user storage
│
├── main.py                 # Application entry point
└── README.md              # Project documentation
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only standard library)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd library-management-system
   ```

2. **Create data directory** (if not exists)
   ```bash
   mkdir -p data
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 🎯 Usage

### Getting Started

Launch the application and you'll see the main menu:

```
Welcome to the Library System
1. View all items
2. Search items
3. Register new user
4. Add new item
5. Borrow item
6. Reserve item
7. Return item
8. Delete item
9. Delete user
10. Save and exit
```

### Common Operations

#### 👤 Register a New User
1. Select option `3`
2. Enter user details when prompted
3. User will be assigned a unique ID

#### 📚 Add New Items
1. Select option `4`
2. Choose item type (Book/Magazine/DVD)
3. Enter item details
4. Item will be added to the library

#### 🔄 Borrow/Return Items
- **Borrow**: Select option `5`, provide user ID and item ID
- **Return**: Select option `7`, provide user ID and item ID

#### 🔖 Reserve Items
1. Select option `6`
2. Provide user ID and item ID
3. Only Books and DVDs support reservations

### Search Functionality

Use option `2` to search for items:
- Search by **title**: Enter partial or full title
- Search by **type**: Enter "book", "magazine", or "dvd"

## 📊 Data Management

### Automatic Persistence
- Data is automatically loaded on startup
- All changes are saved when selecting "Save and exit"
- JSON files store all user and item information

### Data Files
- `data/items.json`: Contains all library items
- `data/users.json`: Contains all registered users

## ⚠️ Exception Handling

The system includes comprehensive error handling:

| Exception | Description |
|-----------|-------------|
| `UserNotFoundError` | User ID doesn't exist |
| `ItemNotFoundError` | Item ID doesn't exist |
| `ItemNotAvailableError` | Item is already borrowed |
| `ReservationError` | Reservation conflicts or unsupported items |

## 🏛️ Architecture

### Class Hierarchy

```
LibraryItem (Abstract Base)
├── Book (+ Reservable)
├── Magazine
└── DVD (+ Reservable)

Reservable (Abstract Interface)
├── Book
└── DVD
```

### Key Components

- **Library**: Central management class
- **User**: Handles user information and borrowed items
- **LibraryItem**: Base class for all library items
- **Reservable**: Interface for items that can be reserved

## 🔧 Development

### Adding New Item Types

1. Create new class inheriting from `LibraryItem`
2. Implement required abstract methods
3. Add `Reservable` interface if needed
4. Update the main menu logic

### Extending Functionality

The modular design allows easy extension:
- Add new item types
- Implement additional search filters
- Add user roles and permissions
- Integrate with external databases

## 📝 Example Usage

```python
# Example of programmatic usage
from models.library import Library
from models.user import User
from models.book import Book

# Create library instance
library = Library()

# Add a user
user = User("123","John Doe", "john@email.com")
library.add_user(user)

# Add a book
book = Book("123456789","Python Programming", "Jane Smith", "Programming")
library.add_item(book)

# Borrow the book
library.borrow_item(user.user_id, book.item_id)
```

## 📞 Contact

**Developer**: Rand Haymouni  
**Email**: [randhaymouni@gmail.com](mailto:randhaymouni@gmail.com)

---
```

