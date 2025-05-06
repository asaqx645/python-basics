from functools import reduce

# Named function to multiply two numbers
def multiply(x, y):
    return x * y
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Use reduce with the multiply function
product = reduce(multiply, numbers)
print("Product of all numbers:", product)


def add(x, y):
    return x + y

def sum_list(numbers):
    """
    Returns the sum of a list using reduce and a named function.
    Parameters:
        numbers (list): A list of numeric values.
    Returns:
        int or float: The sum of the list.
    """
    return reduce(add, numbers)

# Example usage:
numbers = [1, 2, 3, 4, 5]
print("Sum using reduce and named function:", sum_list(numbers))

numbers = [1, 2, 3, 4, 5]
squared_lc = [x * x for x in numbers]
print("Squared with list comprehension:", squared_lc)

evens_lc = [x for x in numbers if x % 2 == 0]
print("Even numbers with list comprehension:", evens_lc)

cubed_gt2 = [x**3 for x in numbers if x > 2]
print("Cubed numbers > 2:", cubed_gt2)

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [item for row in matrix for item in row]
print("Flattened matrix:", flattened)


