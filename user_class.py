from datetime import datetime
class Reader:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.purchase_history = []
        self.shelf = []

    def can_afford(self, book_price):
        return self.balance >= book_price
    
    def buy_book(self, book):
            self.shelf.append(book)
            self.balance -= book.price
            self.purchase_history.append({
                "book": book,
                "price": book.price,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            book.available = False
            
    def list_owned_books(self):
        if not self.shelf:
            print("You don't have any books")
        else:
            print("Here are your books!")
            for book in self.shelf:
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
    
    def show_purchase_history(self):
        if not self.purchase_history:
            print("No purchases found.")
            return
        for i, record in enumerate(self.purchase_history, 1):
            book = record["book"]
            print(f"{i}. {book.title} - ${record['price']:.2f} (Bought on {record['date']})")

    def return_book(self, book_to_return):
        for record in self.purchase_history:
            book = record["book"]
            if book.title.lower().strip() == book_to_return.title.lower().strip():
                book.available = True
                self.balance += 0.8 * record["price"] 
                self.purchase_history.remove(record)
                if book in self.shelf:
                    self.shelf.remove(book)
                print(f"You returned {book.title} and received ${0.8 * record['price']:.2f} back.")
                return
        print(f"There's no book with name {book_to_return.title} in your purchases.")