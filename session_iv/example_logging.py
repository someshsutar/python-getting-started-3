"""
Program: Demonstrate Logging in Python

Scenario:
A simple banking application that performs deposits and withdrawals
while recording important events using the logging module.
"""

import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    filename="banking.log",
    filemode="w"        # Overwrite log file each time
)

# Create logger
logger = logging.getLogger(__name__)


class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

        logger.info(f"Account created for {self.account_holder} "
                    f"with balance ₹{self.balance}")

    def deposit(self, amount):

        logger.debug(f"Deposit Request: ₹{amount}")

        if amount <= 0:
            logger.warning("Deposit amount must be greater than zero.")
            return

        self.balance += amount

        logger.info(f"₹{amount} deposited successfully.")
        logger.info(f"Updated Balance = ₹{self.balance}")

    def withdraw(self, amount):

        logger.debug(f"Withdrawal Request: ₹{amount}")

        if amount <= 0:
            logger.warning("Withdrawal amount must be greater than zero.")
            return

        if amount > self.balance:
            logger.error(
                f"Withdrawal failed! Insufficient balance. "
                f"Current Balance = ₹{self.balance}"
            )
            return

        self.balance -= amount

        logger.info(f"₹{amount} withdrawn successfully.")
        logger.info(f"Updated Balance = ₹{self.balance}")

    def check_balance(self):
        logger.info(f"Current Balance = ₹{self.balance}")
        return self.balance


def main():

    logger.info("========== Banking Application Started ==========")

    account = BankAccount("John Doe", 10000)

    account.deposit(5000)

    account.withdraw(2000)

    account.withdraw(20000)      # Generates ERROR

    account.deposit(-500)        # Generates WARNING

    account.check_balance()

    try:
        logger.info("Attempting risky operation...")
        result = 10 / 0
    except Exception:
        logger.exception("Unexpected Exception Occurred")

    logger.critical("Application Closed")


if __name__ == "__main__":
    main()