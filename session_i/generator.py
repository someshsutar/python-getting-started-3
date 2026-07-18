# Program to demonstrate Generators in Python

def square_generator(n):
    """
    Generator function that yields squares of numbers
    from 1 to n.
    """
    for i in range(1, n + 1):
        print(f"Generating square of {i}")
        yield i * i


# Create a generator object
gen = square_generator(5)

print("Using next() function:")
print(next(gen))
print(next(gen))

print("\nUsing for loop to iterate over remaining values:")
for value in gen:
    print(value)