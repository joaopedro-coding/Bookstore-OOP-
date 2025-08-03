from book_class import Book, Library

is_booking = True
book_store = Library()
while is_booking:
    print("\n--- Library Menu ---")
    print("1. Add a book\n2. Remove a book\n3. List all books\n4. Borrow a book\n5. Return a book\n6. Exit")
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        book_name = input("What is the book name? ")
        book_author = input("What is the book author? ")
        book_to_add = Book(book_name, book_author)
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