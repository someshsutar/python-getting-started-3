from multiprocessing import Process
import time
import os


def calculate_payroll(department, employees):
    """
    Simulates payroll calculation for a department.
    """

    print(f"\nProcess ID : {os.getpid()}")
    print(f"Calculating payroll for {department} Department...")

    total_salary = 0

    # Simulate CPU-intensive calculations
    for employee in range(employees):
        salary = 30000 + (employee % 5000)
        bonus = salary * 0.10
        tax = salary * 0.05

        total_salary += salary + bonus - tax

    print(f"{department} Department Payroll Completed")
    print(f"Total Payroll = ₹{total_salary:,.2f}")


def main():

    departments = [
        ("HR", 500000),
        ("IT", 600000),
        ("Finance", 400000),
        ("Sales", 700000)
    ]

    processes = []

    start = time.time()

    print("===== Payroll Processing Started =====")

    for department, employees in departments:
        process = Process(
            target=calculate_payroll,
            args=(department, employees)
        )

        processes.append(process)
        process.start()

    # Wait for all processes
    for process in processes:
        process.join()

    end = time.time()

    print("\n=====================================")
    print("All Department Payrolls Completed")
    print(f"Total Execution Time : {end - start:.2f} seconds")


if __name__ == "__main__":
    main()