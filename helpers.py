
def welcome_message():
    """
    This is the doctring for welcome message
    """
    return "Welcome to Day 17 - Modules and Imports" 

def custom_message(name):
    """this is the custom message func 
    in side the helpers.py module 

    Args:
        name (str): custom name
    Returns:
        str: name f string 
    """
    return f"Hi Everyone, My name is {name}, Im from the Helpers Python File."

def calculate_square_area(side_length):
    """function to calculate the area of a square in the helpers module

    Args:
        side_length (float): side of a square

    Returns:
        float: value of the 
    """
    return float(side_length ** 2)