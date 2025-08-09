class Reader:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.owned_books = []

    def can_afford(self, book_price):
        return self.balance >= book_price
    
    def buy_book(self, book):
            self.owned_books.append(book)
            self.balance -= book.price
            book.available = False
            
    def list_owned_books(self):
        if not self.owned_books:
            print("You don't have any books")
        else:
            print("Here are your books!")
            for book in self.owned_books:
                book_title = book.title.title()
                book_author = book.author.title()
                book_price = book.price
                print("*********************************")
                print(f"You have {book_title} by {book_author}.\nValue: ${book_price} ")

    def show_balance(self):
        print(f"User balance: ${self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Please insert a valid value.")
        else:
            self.balance += amount
            print(f"You deposited ${amount}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please insert a valid amount.")
        elif self.balance < amount:
            print("You don't have enough money to withdraw.")
        else:
            self.balance -= amount
            print(f"You withdrawn ${amount}.")      