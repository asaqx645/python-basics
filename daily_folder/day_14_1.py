'''Conceptual Notes:
map() is for transforming each element.
filter() is for selecting elements based on a condition.
reduce() is for combining elements into a single result.
These tools relate to the MapReduce paradigm in big data, where:
Map: data is distributed and transformed.
Reduce: data is aggregated into results.
'''

from functools import reduce

# === 1. Using map(): Apply a function to every item in an iterable ===
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print("Original:", numbers)
print("Squared with map():", squared)

# === 2. Using filter(): Select items that match a condition ===
def is_even(x):
    return x % 2 == 0

evens = list(filter(is_even, numbers))
print("Even numbers with filter():", evens)

# === 3. Using reduce(): Accumulate values into a single result ===
def multiply(x, y):
    return x * y

from functools import reduce


product = reduce(multiply, numbers)
print("Product with reduce():", product)

# === 4. Using lambda with map/filter/reduce ===
cubed = list(map(lambda x: x ** 3, numbers))
print("Cubed with lambda + map:", cubed)

odds = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers with lambda + filter:", odds)

sum_total = reduce(lambda x, y: x + y, numbers)
print("Sum with lambda + reduce:", sum_total)
