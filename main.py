class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False
    def update_book(self, title, new_title=None, new_author=None, new_year=None):
        for book in self.books:
            if book.title == title:
                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                if new_year:
                    book.year = new_year
                return True
        return False
    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")
# create a library object
library = Library()
while True:
    print("------------------------Menu------------------------\n1. Add book\n2. Update book\n3. Remove book\n4. Search book\n5. Display books\n6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter year of publication: ")
        book = Book(title, author, year)
        library.add_book(book)
        print("Book added successfully.")
    elif choice == "2":
        title = input("Enter book title: ")
        new_title = input("Enter new title (press enter to skip): ")
        new_author = input("Enter new author (press enter to skip): ")
        new_year = input("Enter new year (press enter to skip): ")
        if library.update_book(title, new_title, new_author, new_year):
            print("Book updated successfully.")
        else:
            print("Book not found.")
    elif choice == "3":
        title = input("Enter book title: ")
        if library.remove_book(title):
            print("Book removed successfully.")
        else:
            print("Book not found.")
    elif choice == "4":
        title = input("Enter book title: ")
        book = library.search_book(title)
        if book:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")
        else:
            print("Book not found.")
    elif choice == "5":
        library.display_books()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Try again.")
