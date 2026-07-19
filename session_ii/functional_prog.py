"""
Program : Functional Programming in Python
Example : E-Commerce Order Processing System

Concepts Demonstrated
---------------------
1. First-Class Functions
2. Higher-Order Functions
3. Lambda Functions
4. map()
5. filter()
6. reduce()
7. zip()
8. any()
9. all()
10. List Comprehension
11. Generator Expression
12. Pure Function
13. Immutability
"""

from functools import reduce

# ------------------------------------------------------
# Sample Order Data
# ------------------------------------------------------

orders = [
    {"id": 101, "customer": "Alice", "amount": 1200, "paid": True},
    {"id": 102, "customer": "Bob", "amount": 4500, "paid": False},
    {"id": 103, "customer": "Charlie", "amount": 1800, "paid": True},
    {"id": 104, "customer": "David", "amount": 5200, "paid": True},
    {"id": 105, "customer": "Eva", "amount": 3200, "paid": False},
]

print("=" * 70)
print("ORIGINAL ORDERS")
print("=" * 70)

for order in orders:
    print(order)

# ======================================================
# 1. First-Class Function
# ======================================================

print("\n1. FIRST-CLASS FUNCTION")

def calculate_tax(amount):
    return amount * 0.18

# Assign function to another variable
tax_function = calculate_tax

print("Tax on ₹5000 =", tax_function(5000))

# ======================================================
# 2. Higher-Order Function
# ======================================================

print("\n2. HIGHER-ORDER FUNCTION")

def apply_discount(func, amount):
    return func(amount)

discount = lambda amount: amount * 0.90

print("Discounted Price =", apply_discount(discount, 5000))

# ======================================================
# 3. Lambda Function
# ======================================================

print("\n3. LAMBDA FUNCTION")

gst = lambda amount: amount * 0.18

print("GST on 2500 =", gst(2500))

# ======================================================
# 4. map()
# ======================================================

print("\n4. map()")

discounted_amounts = list(
    map(lambda order: order["amount"] * 0.90, orders)
)

print("Discounted Amounts")

for amount in discounted_amounts:
    print(amount)

# ======================================================
# 5. filter()
# ======================================================

print("\n5. filter()")

premium_orders = list(
    filter(lambda order: order["amount"] > 3000, orders)
)

print("Premium Orders")

for order in premium_orders:
    print(order)

# ======================================================
# 6. reduce()
# ======================================================

print("\n6. reduce()")

total_sales = reduce(
    lambda total, order: total + order["amount"],
    orders,
    0
)

print("Total Sales =", total_sales)

# ======================================================
# 7. zip()
# ======================================================

print("\n7. zip()")

customers = [order["customer"] for order in orders]
amounts = [order["amount"] for order in orders]

customer_orders = list(zip(customers, amounts))

print("Customer and Amount")

for item in customer_orders:
    print(item)

# ======================================================
# 8. any()
# ======================================================

print("\n8. any()")

payment_status = [order["paid"] for order in orders]

print("Any unpaid orders?", any(not status for status in payment_status))

# ======================================================
# 9. all()
# ======================================================

print("\n9. all()")

print("Are all orders paid?", all(payment_status))

# ======================================================
# 10. List Comprehension
# ======================================================

print("\n10. LIST COMPREHENSION")

customer_names = [
    order["customer"]
    for order in orders
]

print(customer_names)

# ======================================================
# 11. Generator Expression
# ======================================================

print("\n11. GENERATOR EXPRESSION")

revenue_generator = (
    order["amount"]
    for order in orders
)

print("Processing Revenue")

for amount in revenue_generator:
    print(amount)

# ======================================================
# 12. Pure Function
# ======================================================

print("\n12. PURE FUNCTION")

def final_price(price, discount_percent):
    return price - (price * discount_percent / 100)

print(final_price(5000, 10))
print(final_price(5000, 10))

# Same input -> Same output

# ======================================================
# 13. Immutability
# ======================================================

print("\n13. IMMUTABILITY")

original_status = ("Pending", "Packed", "Shipped")

print("Original")
print(original_status)

updated_status = original_status + ("Delivered",)

print("Updated")
print(updated_status)

# ======================================================
# 14. Functional Programming Pipeline
# ======================================================

print("\n14. COMPLETE FUNCTIONAL PIPELINE")

result = reduce(
    lambda total, amount: total + amount,
    map(
        lambda order: order["amount"] * 0.90,
        filter(
            lambda order: order["amount"] > 2000,
            orders
        )
    ),
    0
)

print("Revenue after Discount =", result)

# ======================================================
# 15. Generator + Sum
# ======================================================

print("\n15. GENERATOR + SUM")

total = sum(
    order["amount"]
    for order in orders
)

print("Grand Total =", total)

print("\nProgram Completed Successfully.")