class Library:
    
    def __init__(self):
        self.shelf = []

    def find_book(self, book_title):
        for book in self.shelf:
            if book.title.lower().strip() == book_title.lower().strip():
                return book
        return None

    def add_book(self, book):
        if self.find_book(book.title):
            print(f"{book.title.title()} is already on the shelf.")
            return
        self.shelf.append(book)
        print(f"{book.title.title()} was added to the shelf.")


    def remove_book(self, book_title):
        book = self.find_book(book_title)
        if book:
            self.shelf.remove(book)
            print(f"{book_title.capitalize().title()} was removed from your shelf")
            return
        print(f"No book was found with the name {book_title.title()}")
    
    def list_books(self):
        if not self.shelf:
            print("Your shelf is empty.")
        else:
            print("Here are your books!")
            for book in self.shelf:
                book_title = book.title.title()
                book_author = book.author.title()
                book_availabity = book.available
                print("*********************************")
                print(f"{book_title} by {book_author}. Is available: {book_availabity}")

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