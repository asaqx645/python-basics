import math
# -----------------------------
# Defining and Calling Functions
# -----------------------------

def greeting(name): 
    output = f"Hi there, my name is {name}!"
    return print(output)
greet = greeting(name='Adi')

def squared(number):
    return number * number
result = squared(15006)
print(f"The square of 15006: {result}")

def introductions(name, age=50):
    output = print(f"My name is {name} and I am {age} years old!")
    return output

intro_1 = introductions(name='shawn')
intro_2 = introductions(name='drew', age=25)

sqrt = math.sqrt(49000000000000000000000000000000000000000000000)
cosine0 = math.cos(0)
print(sqrt)
print(cosine0)
pi_val = math.pi
print(f"{pi_val}")

# farenheit = 98.6
input_fahrenheit = float(input("enter the temp in farenheit: "))
celsius = (5 / 9) * (input_fahrenheit - 32)  # PEMDAS/BODMAS
def fahrenheit_to_celsius(temp_c):
    return temp_c
temperature_celcius = fahrenheit_to_celsius(celsius)
print(f"Temperature in Celsius: {temperature_celcius:.2f}")

