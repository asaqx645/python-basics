""" map() - is for transforming each element
    map(f, [x1, x2, x3]) -> [f(x1), f(x2), f(x3)]
    filter() is for selecting elements based on a condition
    filter(f, [x1, x2, x3]) -> [xi for which x1 == True]) 
    reduce() is for combining elements into a single result
    reduce(f, [x1, x2, x3, x4, x5]) -> [(((f(x1, x2) x3) x4) x5)])
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]

squared = [ x * x for x in numbers]
print(squared)

squared_1 = []
def squared(numbers):
    for x in numbers:
        y = x * x
        squared_1.append(y)
squared(numbers)
print("squared_1 : ", squared_1)

even_lc= [x for x in numbers if x % 2 == 0] # filter()
print("even_lc: ",even_lc)

odd_lc= [x for x in numbers if x % 2 != 0]
print("odd_lc: ",odd_lc)

matrix = [[1, 2], [3, 4], [5, 6]] # list of lists, and we made it into a single list
flattened = [item for row in matrix for item in row]
print("flattened: ", flattened)

numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(x):
    return x * x

obj1 = list(map(lambda x : x*x, numbers_1))
obj2 = list(map(square, numbers_1))
print("obj1: ", obj1)
print("obj2: ", obj2)

def even_func(x):
     return x % 2 == 0
def odd_func(x):
     return x % 2 != 0

obj3 = list(filter(even_func, numbers_1))
obj4 = list(filter(lambda x: x % 2 == 0, numbers_1))
print("obj3: ", obj3)
print("obj4: ", obj4)

obj5 = list(filter(odd_func, numbers_1))
obj6 = list(filter(lambda x: x % 2 != 0, numbers_1))
print("obj5: ", obj5)
print("obj5_type: ", type(obj5))
print("obj6: ", obj6)

def multiply(x, y):
    return x * y
   
    
obj7 = reduce(multiply, numbers)
obj8 = reduce(multiply, numbers_1)
obj9 = reduce(lambda x, y : x + y , numbers)
obj10 = reduce(lambda x, y : x + y , numbers_1)

print(obj7)
print(obj8)
print(obj9)
print(obj10)



