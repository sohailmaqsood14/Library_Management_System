class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("_______________ ")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        for book in self.books:
            book.display_info()

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.display_info()
                return

        print("Book not found.")

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed.")
                return

        print("Book ID not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    print("Book returned successfully!")
                else:
                    print("This book was not borrowed.")
                return

        print("Book ID not found.")


# Creating library object
library = Library()

# Creating book objects
book1 = Book(1, "Python Basics", "John")
book2 = Book(2, "OOP in Python", "David")
book3 = Book(3, "Data Structures", "Alex")

# Adding books
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Menu
while True:
    print("\n LIBRARY MANAGEMENT SYSTEM")
    print("1. Display All Books")
    print("2. Add Book")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        new_book = Book(book_id, title, author)
        library.add_book(new_book)

    elif choice == "3":
        title = input("Enter Book Title: ")
        library.search_book(title)

    elif choice == "4":
        book_id = int(input("Enter Book ID: "))
        library.borrow_book(book_id)

    elif choice == "5":
        book_id = int(input("Enter Book ID: "))
        library.return_book(book_id)

    elif choice == "6":
        print("Thank you for using the Library System!")
        break

    else:
        print("Invalid choice. Try again.")
