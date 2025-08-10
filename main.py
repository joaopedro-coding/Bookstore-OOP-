from book_class import Book
from bookstore_class import Library
from user_class import Reader
from books import initial_books

is_creating_user = True
readers = []
book_store = Library()

for livro in initial_books:
    new_book = Book(livro["title"], livro["author"], livro["price"])
    new_book.available = livro["available"]
    book_store.add_book(new_book)

while is_creating_user:
    print("\n--- User Menu ---")
    print("1. Create user")
    print("2. Buy book")
    print("3. List owned books")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Show balance")
    print("7. Return book")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    if choice == "1":
        user_name = input("What is your name? ")
        if book_store.find_user(user_name, readers):
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
        reader = book_store.get_existing_user(readers)
        if reader:
            book_store.list_books_with_index()
            book = book_store.choose_book_by_number(book_store)
            if not book.available:
                print("Book is not available.")
            elif not reader.can_afford(book.price):
                print("You don't have enough balance to buy this book.")
            else:
                reader.buy_book(book)
                print(f"{reader.name} bought {book.title} by ${book.price}")
                print(f"{reader.name} balance: ${reader.balance:.2f}")
                
    elif choice == "3":
        reader = book_store.get_existing_user(readers)
        if reader:
            reader.list_owned_books()

    elif choice == "4":
        reader = book_store.get_existing_user(readers)
        if reader:
            while True:
                try:
                    deposit = float(input("How much money do you want to deposit? $"))
                    reader.deposit(deposit)
                    break
                except ValueError:
                    print("Please insert a valid value.")
    
    elif choice == "5":
        reader = book_store.get_existing_user(readers)
        if reader:
            while True:
                try:
                    withdraw = float(input("How much money do you want to withdraw? $"))
                    reader.withdraw(withdraw)
                    break
                except ValueError:
                    print("Please insert a valid value.")

    elif choice == "6":
        reader = book_store.get_existing_user(readers)
        if reader:
            reader.show_balance()

    elif choice == "7":
        reader = book_store.get_existing_user(readers)
        if reader:
            reader.show_purchase_history()
            book = book_store.choose_book_by_number(reader)
            reader.return_book(book)

    elif choice == "8":
        print("Thanks for using the program!")
        is_creating_user = False
    
    elif choice == "set promotion":
        book_store.list_books_with_index()
        book = book_store.choose_book_by_number(book_store)
        if book:
            while True:
                try:
                    discount = int(input("Choose a discount(0-100): "))
                    book.set_promotion(discount)
                    break
                except ValueError:
                    print("Please choose a valid option")
        else:
            print("No book found.")

    elif choice == "remove promotion":
        book_store.list_books_with_index()
        book = book_store.choose_book_by_number(book_store)
        if book:
            if book.on_sale:
                book.remove_promotion()
            else:
                print("Book is not on sale")
        else:
            print("No book found.")
    else:
        print(f"{choice} is not a valid option.")

