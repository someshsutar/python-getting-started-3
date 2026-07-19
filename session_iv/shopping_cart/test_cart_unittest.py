import unittest
from cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Laptop", 50000, 2)

        self.assertEqual(len(self.cart.items), 1)

    def test_total(self):
        self.cart.add_item("Laptop", 50000, 2)
        self.cart.add_item("Mouse", 1000, 3)

        self.assertEqual(self.cart.calculate_total(), 103000)

    def test_discount(self):
        self.cart.add_item("Laptop", 50000, 2)

        self.assertEqual(
            self.cart.apply_discount(10),
            90000
        )

    def test_remove_item(self):
        self.cart.add_item("Laptop", 50000, 1)

        self.cart.remove_item("Laptop")

        self.assertEqual(len(self.cart.items), 0)

    def test_invalid_quantity(self):

        with self.assertRaises(ValueError):
            self.cart.add_item("Laptop", 50000, 0)

    def test_invalid_price(self):

        with self.assertRaises(ValueError):
            self.cart.add_item("Laptop", -1000, 2)

    def test_invalid_discount(self):

        self.cart.add_item("Laptop", 50000, 1)

        with self.assertRaises(ValueError):
            self.cart.apply_discount(150)

    def test_remove_invalid_item(self):

        with self.assertRaises(KeyError):
            self.cart.remove_item("Phone")


if __name__ == "__main__":
    unittest.main()