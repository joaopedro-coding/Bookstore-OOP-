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



    def remove_book(self, book_title):
        book = self.find_book(book_title)
        if book:
            self.shelf.remove(book)
            print(f"{book_title.capitalize().title()} was removed from your shelf")
            return
        print(f"No book was found with the name {book_title.title()}")
    
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

    def borrow_book(self, book_title):
        book = self.find_book(book_title)
        if book:
            if book.available:
                print(f"{book_title.title()} was borrowed. Good reading 📚")
                book.available = False
            else:
                print(f"{book_title.title()} is not available. Someone is reading it already.")
            return
        print(f"No book found with the title {book_title.title()}.")


    def return_book(self, book_title):
        book = self.find_book(book_title)
        if book:
            if not book.available:
                print(f"{book_title.title()} was returned to the shelf.")
                book.available = True
            else:
                print(f"{book_title.title()} is already available. No need to return.")
            return
        print(f"No book found with the title {book_title.title()}.")