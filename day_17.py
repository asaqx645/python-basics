import math
import random
from datetime import datetime
import helpers # this is the custom module

name = 'Aditya'
side = 9872354.0987
print('welcome msg >>>>>>>>', helpers.welcome_message())
print('THIS IS THE DOCSTRING FROM HELPERS: ', helpers.welcome_message.__doc__)
print("Docstring custom message: \n", helpers.custom_message.__doc__)
print(helpers.calculate_square_area(side_length=side))
print("value of pi: ",  math.pi)
print("value of e: ",  math.e)
print("value of tau: ",  math.tau)
print("value of inf: ",  math.inf)
print("value of nan: ",  math.nan)
# sin(45) = 0.707106781
print("sin(45): ", 1/math.sqrt(2))
students = ["Aditya", "Sean", "Jason", "Michelle", "John"]
print(random.choice(students))
print([random.choices(students), random.choices(students)])

time_now = datetime.now()
day_now = datetime.now().day
print (f"Current Time is: {time_now}" )
print (f"Current day is: {day_now}" )
timestamp = time_now.strftime("%Y-%m-%d %H:%M:%S")
print("timestamp: ", timestamp)