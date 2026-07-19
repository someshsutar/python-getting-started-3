import pytest
from cart import ShoppingCart


@pytest.fixture
def cart():
    return ShoppingCart()


def test_add_item(cart):
    cart.add_item("Laptop", 50000, 2)

    assert len(cart.items) == 1


def test_total(cart):
    cart.add_item("Laptop", 50000, 2)
    cart.add_item("Mouse", 1000, 3)

    assert cart.calculate_total() == 103000


def test_discount(cart):
    cart.add_item("Laptop", 50000, 2)

    assert cart.apply_discount(10) == 90000


def test_remove_item(cart):
    cart.add_item("Laptop", 50000, 1)

    cart.remove_item("Laptop")

    assert len(cart.items) == 0


def test_invalid_quantity(cart):

    with pytest.raises(ValueError):
        cart.add_item("Laptop", 50000, 0)


def test_invalid_price(cart):

    with pytest.raises(ValueError):
        cart.add_item("Laptop", -100, 2)


def test_invalid_discount(cart):

    cart.add_item("Laptop", 50000, 1)

    with pytest.raises(ValueError):
        cart.apply_discount(150)


def test_remove_invalid_item(cart):

    with pytest.raises(KeyError):
        cart.remove_item("Phone")