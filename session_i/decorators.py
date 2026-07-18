import time
from functools import wraps

# Simulate user login
logged_in = True


# Decorator 1: Logging
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Calling function: {func.__name__}")
        print(f"[LOG] Arguments: {args}")
        result = func(*args, **kwargs)
        print(f"[LOG] Function '{func.__name__}' completed.")
        return result
    return wrapper


# Decorator 2: Execution Timer
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] Execution Time: {end - start:.4f} seconds")
        return result
    return wrapper


# Decorator 3: Authentication
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not logged_in:
            print("[ERROR] Access Denied! Please login.")
            return
        return func(*args, **kwargs)
    return wrapper


# Decorator 4: Validate Positive Numbers
def validate_positive(func):
    @wraps(func)
    def wrapper(a, b):
        if a < 0 or b < 0:
            print("[ERROR] Only positive numbers are allowed.")
            return
        return func(a, b)
    return wrapper


# -----------------------------
# Function 1: Addition
# -----------------------------
@logger
@timer
@validate_positive
def add(a, b):
    """Returns addition of two positive numbers."""
    time.sleep(1)        # Simulate processing
    print("Addition =", a + b)


# -----------------------------
# Function 2: Dashboard Access
# -----------------------------
@logger
@login_required
def dashboard():
    """Displays dashboard."""
    print("Welcome to the Dashboard!")


# -----------------------------
# Main Program
# -----------------------------
print("===== Python Decorator Demonstration =====")

dashboard()

add(10, 20)

add(-5, 15)

print("\nFunction Name :", add.__name__)
print("Doc String    :", add.__doc__)