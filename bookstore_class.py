class Library:
    
    def __init__(self):
        self.shelf = []

    def find_book(self, book_title):
        for book in self.shelf:
            if book.title.lower().strip() == book_title.lower().strip():
                return book
        return None

    def add_book(self, book):
        self.shelf.append(book)
    
    def list_books_with_index(self):
        if not self.shelf:
            print("Your shelf is empty.")
            return

        print("Here are the books!")
        for i, book in enumerate(self.shelf, 1):
            status = "✅ Available" if book.available else "❌ Unavailable"
            print("*********************************")
            print(f"{i}. {book.title.title()} by {book.author.title()}")
            print(f"Price: ${book.price:.2f}")
            print(f"Status: {status}")