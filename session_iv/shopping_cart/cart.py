class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if price < 0:
            raise ValueError("Price cannot be negative")

        self.items[item] = {
            "price": price,
            "quantity": quantity
        }

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            raise KeyError("Item not found")

    def calculate_total(self):
        total = 0

        for item in self.items.values():
            total += item["price"] * item["quantity"]

        return total

    def apply_discount(self, percentage):

        if percentage < 0 or percentage > 100:
            raise ValueError("Invalid discount percentage")

        total = self.calculate_total()

        return total - (total * percentage / 100)