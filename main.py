from book_class import Book
from bookstore_class import Library
from user_class import Reader
from books import initial_books

is_creating_user = True
readers = []
book_store = Library()

def find_user(user_name):
    for reader in readers:
        if reader.name.lower().strip() == user_name.lower().strip():
            return reader
    return None

def choose_book_by_number(library):
    while True:
        try:
            choice = int(input("Enter the number of the book you want: "))
            if 1 <= choice <= len(library.shelf):
                return library.shelf[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(library.shelf)}.")
        except ValueError:
            print("Please enter a valid number.")

def choose_reader_by_number(reader_lis):
    while True:
        try:
            choice = int(input("Enter the number of the reader you want: "))
            if 1 <= choice <= len(reader_lis):
                return reader_lis[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(reader_lis)}.")
        except ValueError:
            print("Please enter a valid number.")

def get_existing_user(reader_list):
    display_readers(reader_list)
    reader = choose_reader_by_number(reader_list)
    if not reader:
        print(f"No user found with the name {reader.name}.")
    return reader

def display_readers(reader_list):
    for i, book_reader in enumerate(reader_list, 1):
        print(f"{i}. {book_reader.name}")

for livro in initial_books:
    new_book = Book(livro["title"], livro["author"], livro["price"])
    new_book.available = livro["available"]
    book_store.add_book(new_book)


while is_creating_user:
    print("\n--- User Menu ---")
    print("1. Create user")
    print("2. Buy book")
    print("3. List owned books")
    print("4. Show balance")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        user_name = input("What is your name? ")
        if find_user(user_name):
            print("User already exists.")
        else:
            while True:
                try:
                    user_balance = float(input("What is your balance? $"))
                    break
                except ValueError:
                    print("Please enter a valid number.")
            readers.append(Reader(user_name, user_balance))
            print(f"Welcome {user_name} to the Library. Your balance is: ${user_balance:.2f}")

    elif choice == "2":
        reader = get_existing_user(readers)
        if reader:
            book_store.list_books_with_index()
            book = choose_book_by_number(book_store)
            if book.available:
                reader.buy_book(book)
                print(f"{reader.name} bought {book.title} by ${book.price}")
                print(f"{reader.name} balance: ${reader.balance:.2f}")
            else:
                print(f"{book.title} is not available to buy!")

    elif choice == "3":
        reader = get_existing_user(readers)
        if reader:
            reader.list_owned_books()

    elif choice == "4":
        reader = get_existing_user(readers)
        if reader:
            reader.show_balance()

    elif choice == "5":
        print("Thanks for using the program!")
        is_creating_user = False

    else:
        print(f"{choice} is not a valid option.")

