# Program to demonstrate Iterators in Python

class NumberIterator:
    """
    Custom iterator that generates numbers from 1 to a given limit.
    """

    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    # Returns the iterator object itself
    def __iter__(self):
        return self

    # Returns the next value
    def __next__(self):
        if self.current <= self.limit:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration


# Create an iterator object
numbers = NumberIterator(5)

print("Using next() function:")
print(next(numbers))
print(next(numbers))

print("\nUsing for loop to iterate over remaining values:")
for num in numbers:
    print(num)