import json

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False

    def to_dict(self):
        return {
            "Book ID": self.book_id,
            "Title": self.title,
            "Author": self.author,
            "Issued": self.issued
        }


class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book.to_dict())

        self.save_books()
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nLibrary Books:")
        for book in self.books:
            print(book)

    def search_book(self):
        keyword = input("Enter title or author name: ").lower()

        found = False

        for book in self.books:
            if keyword in book["Title"].lower() or keyword in book["Author"].lower():
                print(book)
                found = True

        if not found:
            print("No matching books found.")

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        for book in self.books:
            if book["Book ID"] == book_id:
                if not book["Issued"]:
                    book["Issued"] = True
                    self.save_books()
                    print("Book issued successfully!")
                else:
                    print("Book already issued.")
                return

        print("Book not found.")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:
            if book["Book ID"] == book_id:
                if book["Issued"]:
                    book["Issued"] = False
                    self.save_books()
                    print("Book returned successfully!")
                else:
                    print("Book was not issued.")
                return

        print("Book not found.")

    def save_books(self):
        with open("library.json", "w") as file:
            json.dump(self.books, file, indent=4)

    def load_books(self):
        try:
            with open("library.json", "r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []


library = Library()

while True:
    print("\n--- Library Book Inventory Manager ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please try again.")