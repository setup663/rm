class Tv:
    def __init__(self, model, diag, price):
        self.model = model
        self.diag = diag
        self.price = price
    def __str__(self):
        return f"телевизоры:{self.model} {self.diag} {self.price}"