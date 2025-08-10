class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.original_price = price
        self.price = price
        self.on_sale = False
        self.available = True

    def set_promotion(self, discount):
        if discount <= 0 or discount > 100:
            print("Invalid discount value.")
            return
        if not self.on_sale:
            self.on_sale = True
            self.price = self.original_price * (1 - discount / 100)
            print(f"Promotion activated: {self.title} is now ${self.price:.2f}")
        else:
            print("Book is already on sale")

    def remove_promotion(self):
        self.on_sale = False
        self.price = self.original_price
        print(f"Promotion removed for {self.title}.")