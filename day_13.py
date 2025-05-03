import math
def welcome_student(name):
    return print(f"Hi Everyone, My name is {name}!")

def print_courses(name, *courses):
    print(type(*courses))
    print(type(courses))
    return print(f"Hi Everyone, My name is {name}!, and Im going to take {courses}")

def total_credits(*credits):
    print( 'what was passed to the total credits function: ', *credits)
    return print(f"Total Credits: {[sum(credits)]}")

def display_profile(git**student_profile):
    print(student_profile['name'])
    for key, value in student_profile.items():
        print(f"key: {key} value: {value}")
    print(type(student_profile))    
    return print(student_profile)

def square_reg(x):
    squared_out = x*x
    return print(squared_out)

# lambda arguments: expression
square = lambda x: x*x # square is the varible that can be printed 
# = is the assignment and lambda keyword is precursor to the argument of the function 
# name square and after :, we have the espression, and in our case operation

if __name__=="__main__":
    square_reg(2)
    print(type(square(10)))
    print(square(10))
    name = "shawn"
    courses = ["AI", "Stats", "ML"]
    credits = [4, 4, 4]
    student_profile =     {
        "name": "Shawn",
        "program": "MSDS",
        "grades": [
            3.5,
            3.6,
            3.7
        ]
    }
    
    welcome_student(name)
    print_courses(name, courses)
    total_credits(234, 23432, 1234312432432, 654)
    display_profile(**student_profile)
    display_profile(name='adi', program='computer science', grades=[99.0])  # *args & **kwargs
   