class Product:
    def __init__(self, name, owner, starting_price):
        self.name = name
        self.owner = owner
        self.starting_price = starting_price
        self.highest_bid = starting_price
        self.highest_bidder = None

    def place_bid(self, bidder, bid_amount):
        if bid_amount > self.highest_bid:
            self.highest_bid = bid_amount
            self.highest_bidder = bidder
            return True
        return False

    def __str__(self):
        return f"{self.name} (Proprietar: {self.owner}, Pret Initial: {self.starting_price}, Pret Maxim: {self.highest_bid})"
