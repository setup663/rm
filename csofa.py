class Sofa:
    def __init__(self, material, color, price):
        self.material = material
        self.color = color
        self.price = price

    def __str__(self):
        return f"диваны:{self.material} {self.color} {self.price}"