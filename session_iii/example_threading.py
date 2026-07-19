import threading
import time
import random


def process_order(order_id, customer_name):
    """Simulates processing of a customer order."""

    print(f"\n Order {order_id} received from {customer_name}")

    # Step 1: Payment Verification
    print(f"Order {order_id}: Verifying payment...")
    time.sleep(random.randint(1, 3))

    # Step 2: Packaging
    print(f"Order {order_id}: Packaging product...")
    time.sleep(random.randint(1, 3))

    # Step 3: Shipping
    print(f"Order {order_id}: Shipping product...")
    time.sleep(random.randint(1, 3))

    print(f" Order {order_id} completed for {customer_name}")


def main():

    customers = [
        (101, "Alice"),
        (102, "Bob"),
        (103, "Charlie"),
        (104, "David"),
        (105, "Eva")
    ]

    threads = []

    start_time = time.time()

    print("===== Online Shopping Order Processing =====")

    for order_id, customer in customers:
        thread = threading.Thread(
            target=process_order,
            args=(order_id, customer),
            name=f"Order-{order_id}"
        )

        threads.append(thread)
        thread.start()

    # Wait for all orders to complete
    for thread in threads:
        thread.join()

    end_time = time.time()

    print("\n======================================")
    print("All customer orders processed successfully.")
    print(f"Total Time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()