import json

# === Global variable for demonstration ===
school_name = "Arizona State University"

# === Function 1: Greet Student ===
def greet_student(name):
    return "Hello, I'm %s, and I'm a student at ASU." % name

# === Function 2: Compute GPA ===
def compute_gpa(grades):
    if not grades:
        return 0.0
    return round(sum(grades) / len(grades), 3)

# === Function 3: Honor Roll Check ===
def is_on_honor_roll(gpa):
    return gpa >= 3.7

# === Function 4: Print Student Info using Global Scope ===
def print_student_info(name, gpa):
    department = "Computer Science"
    print(f"{name} is a student in {department} at {school_name}.")
    if is_on_honor_roll(gpa):
        print(f"{name} is on the Honor Roll!\n")
    else:
        print(f"{name} is not on the Honor Roll.\n")

# === Student Class ===
class Student:
    def __init__(self, name, program, grades):
        self.name = name
        self.program = program
        self.grades = grades
        self.gpa = compute_gpa(grades)
    
    def to_dict(self):
        return {
            "name": self.name,
            "program": self.program,
            "grades": self.grades,
            "GPA": self.gpa
        }

# === JSON Input ===
sample_json = 