from book_class import Book
from bookstore_class import Library
from user_class import Reader

is_booking = True
is_creating_user = True
readers = []
book_store = Library()

def find_user(user_name):
    for reader in readers:
        if reader.name.lower().strip() == user_name.lower().strip():
            return reader
    return None

while is_booking:
    print("\n--- Library Menu ---")
    print("1. Add a book\n2. Remove a book\n3. List all books\n4. Borrow a book\n5. Return a book\n6. Exit")
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        book_name = input("What is the book name? ")
        book_author = input("What is the book author? ")
        book_price = float(input("What is the book price? $"))
        book_to_add = Book(book_name, book_author, book_price)
        book_store.add_book(book_to_add)
    elif choice == "2":
        book_name = input("What is the book name? ")
        book_store.remove_book(book_name)
    elif choice == "3":
         book_store.list_books()
    elif choice == "4":
        book_name = input("What book do you want to borrow: ")
        book_store.borrow_book(book_name)
    elif choice == "5":
        book_name = input("What book do you want to return: ")
        book_store.return_book(book_name)
    elif choice == "6":
        is_booking = False
        print("Thanks for using our bookstore.")
    else:
        print(f"{choice} is not a valid option.")

while is_creating_user:
    print("\n--- User Menu ---")
    print("1. Create an user\n2. Buy book\n3. List owned books\n4. Exit")
    user_choice = input("Choose an option (1-2): ")

    if user_choice == "1":
        user_name = input("What is your name? ")
        user_balance = float(input("What is your balance? $"))
        user = Reader(user_name, user_balance)
        readers.append(user)
    elif user_choice == "2":
        user_to_buy = input("Wich user wants to buy? ")
        reader = find_user(user_to_buy)
        if reader:
            book_store.list_books()
            book_name = input("What book do you want to buy? ")
            if book_store.find_book(book_name):
                reader.buy_book(book_name, book_store)
            else:
                print(f"No book was found with the name {book_name}.")
        else:
            print(f"There are no user with the name {user_to_buy}.")
    elif user_choice == "3":
        user_to_list = input("Wich user wants to display the owned books? ")
        reader = find_user(user_to_list)
        if reader:
            reader.list_owned_books()
        else:
            print(f"No user found with the name {user_to_list}")
    elif user_choice == "4":
        is_creating_user = False
    else:
        print(f"{user_choice} is not a valid option.")
