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

def get_existing_user(prompt):
    user_name = input(prompt)
    reader = find_user(user_name)
    if not reader:
        print(f"No user found with the name {user_name}.")
    return reader

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
            print(f"Welcome {user_name} to the Library. Your balance is: ${user_balance}")

    elif choice == "2":
        reader = get_existing_user("Which user wants to buy? ")
        if reader:
            book_store.list_books_with_index()
            book = choose_book_by_number(book_store)
            reader.buy_book(book, book_store)
            print(f"{reader} bought {book.name} by ${book.price}")
            print(f"{reader} balance: ${reader.balance}")

    elif choice == "3":
        reader = get_existing_user("Which user wants to display the owned books? ")
        if reader:
            reader.list_owned_books()

    elif choice == "4":
        reader = get_existing_user("Which user wants to check the balance? ")
        if reader:
            reader.show_balance()

    elif choice == "5":
        print("Thanks for using the program!")
        is_creating_user = False

    else:
        print(f"{choice} is not a valid option.")

