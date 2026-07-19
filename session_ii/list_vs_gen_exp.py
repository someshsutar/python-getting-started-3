"""
Program: List Comprehension vs Generator Expression
Real-world Example: Online Shopping Order Processing
"""

from sys import getsizeof

# Sample order data
orders = [
    {"id": 101, "customer": "Alice", "amount": 1200},
    {"id": 102, "customer": "Bob", "amount": 4500},
    {"id": 103, "customer": "Charlie", "amount": 1800},
    {"id": 104, "customer": "David", "amount": 5200},
    {"id": 105, "customer": "Eva", "amount": 3200},
]

print("=" * 60)
print("Original Orders")
print("=" * 60)

for order in orders:
    print(order)

# ----------------------------------------------------
# Example 1: List Comprehension
# ----------------------------------------------------
print("\n1. LIST COMPREHENSION")
print("-" * 60)

# Apply 10% discount to every order
discounted_orders = [
    {
        "id": order["id"],
        "customer": order["customer"],
        "discounted_amount": order["amount"] * 0.90
    }
    for order in orders
]

print("Orders after 10% discount")

for order in discounted_orders:
    print(order)

# ----------------------------------------------------
# Example 2: Filtering using List Comprehension
# ----------------------------------------------------
print("\n2. FILTER USING LIST COMPREHENSION")
print("-" * 60)

premium_orders = [
    order for order in orders
    if order["amount"] >= 3000
]

print("Premium Orders (>3000)")

for order in premium_orders:
    print(order)

# ----------------------------------------------------
# Example 3: Generator Expression
# ----------------------------------------------------
print("\n3. GENERATOR EXPRESSION")
print("-" * 60)

# Revenue generated lazily
revenue_generator = (
    order["amount"]
    for order in orders
)

print("Generator Object")
print(revenue_generator)

print("\nProcessing Revenue")

for amount in revenue_generator:
    print(amount)

# ----------------------------------------------------
# Example 4: Sum using Generator Expression
# ----------------------------------------------------
print("\n4. TOTAL REVENUE")
print("-" * 60)

total_revenue = sum(
    order["amount"]
    for order in orders
)

print("Total Revenue =", total_revenue)

# ----------------------------------------------------
# Example 5: Memory Comparison
# ----------------------------------------------------
print("\n5. MEMORY COMPARISON")
print("-" * 60)

large_list = [x for x in range(100000)]

large_generator = (
    x for x in range(100000)
)

print("List Size      :", getsizeof(large_list), "bytes")
print("Generator Size :", getsizeof(large_generator), "bytes")

# ----------------------------------------------------
# Example 6: Generator Exhaustion
# ----------------------------------------------------
print("\n6. GENERATOR CAN BE USED ONLY ONCE")
print("-" * 60)

numbers = (x for x in range(5))

print("First Iteration")

for n in numbers:
    print(n)

print("\nSecond Iteration")

for n in numbers:
    print(n)

print("No output because generator is exhausted.")

# ----------------------------------------------------
# Example 7: next()
# ----------------------------------------------------
print("\n7. USING next()")
print("-" * 60)

ids = (order["id"] for order in orders)

print(next(ids))
print(next(ids))
print(next(ids))