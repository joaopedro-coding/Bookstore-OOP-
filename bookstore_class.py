class Library:
    
    def __init__(self):
        self.shelf = []

    def find_book(self, book_reference):
        for book in self.shelf:
            if book.title.lower().strip() == book_reference.lower().strip():
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

    def find_user(self, user_name, readers_list):
        for reader in readers_list:
            if reader.name.lower().strip() == user_name.lower().strip():
                return reader
        return None
    
    def choose_book_by_number(self, library):
        while True:
            try:
                choice = int(input("Enter the number of the book you want: "))
                if 1 <= choice <= len(library.shelf):
                    return library.shelf[choice - 1]
                else:
                    print(f"Please enter a number between 1 and {len(library.shelf)}.")
            except ValueError:
                print("Please enter a valid number.")

    def choose_reader_by_number(self, reader_list):
        while True:
            try:
                choice = int(input("Enter the number of the reader you want: "))
                if 1 <= choice <= len(reader_list):
                    return reader_list[choice - 1]
                else:
                    print(f"Please enter a number between 1 and {len(reader_list)}.")
            except ValueError:
                print("Please enter a valid number.")
    
    def display_readers(self, reader_list):
        for i, book_reader in enumerate(reader_list, 1):
            print(f"{i}. {book_reader.name}")

    def get_existing_user(self, reader_list):
        self.display_readers(reader_list)
        reader = self.choose_reader_by_number(reader_list)
        if not reader:
            print(f"No user found with the name {reader.name}.")
        return reader
    
   