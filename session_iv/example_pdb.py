"""
Program: Demonstrate Debugging with pdb

Scenario:
An online shopping application calculates the final bill after
applying a discount.

The program contains an intentional bug:
Instead of subtracting the discount, it adds the discount.

Use pdb to identify the bug.
"""

import pdb


def calculate_bill(price, quantity, discount_percentage):
    """Calculate the final bill amount."""

    # Breakpoint starts here
    pdb.set_trace()

    total = price * quantity

    discount = total * discount_percentage / 100

    # Intentional Bug
    final_amount = total + discount

    return final_amount


def main():
    print("===== Online Shopping =====")

    price = 50000
    quantity = 2
    discount = 10

    bill = calculate_bill(price, quantity, discount)

    print(f"\nFinal Bill = ₹{bill}")


if __name__ == "__main__":
    main()