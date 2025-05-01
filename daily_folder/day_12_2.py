import json
import os
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

# === Base Class: Person ===
class Person:
    def __init__(self, name, program):
        self.name = name
        self.program = program

    def introduce(self):
        return f"My name is {self.name}, and I am enrolled in the {self.program} program."

# === Derived Class: Student inherits from Person ===
class Student(Person):
    def __init__(self, name, program, grades):
        super().__init__(name, program)
        self.grades = grades
        self.gpa = compute_gpa(grades)

    def to_dict(self):
        return {
            "name": self.name,
            "program": self.program,
            "grades": self.grades,
            "GPA": self.gpa
        }

    def __str__(self):
        return f"{self.name} - {self.program} - GPA: {self.gpa}"

# === JSON Input ===
sample_json = """[
    {"name": "Aditya", "program": "MSCS", "grades": [4.0, 3.8, 3.9]},
    {"name": "Shawn", "program": "MSDS", "grades": [3.5, 3.6, 3.7]},
    {"name": "Drew", "program": "MBA", "grades": [3.2, 3.3, 3.1]}
]"""

# === Process Students and Demonstrate Function Use ===
def process_students(json_data):
    student_data = json.loads(json_data)
    student_objects = []
    for data in student_data:
        student = Student(data['name'], data['program'], data['grades'])
        student_objects.append(student)
        print("-" * 40)
        print(student.introduce())  # inherited method
        print(greet_student(student.name))
        print(f"GPA: {student.gpa}")
        print(f"Grades: {student.grades}")
        print(f"Program: {student.program}")
        print_student_info(student.name, student.gpa)
    return student_objects

# === Save to JSON File ===.
filename = 'day-12-students.json'
current_dir = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(current_dir, filename)
print(full_path)

def save_students_to_file(students, filename):
    try:
        with open(full_path, 'w') as f:
            lst = json.loads(sample_json)
            string_for_write = json.dumps(lst, indent=4, ensure_ascii=True)
            f.write((string_for_write))
        print(f"Student data saved to {full_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

save_students_to_file(sample_json, full_path)
    
# === Load from JSON File ===
def load_students_from_file(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return [Student(d['name'], d['program'], d['grades']) for d in data]

# === Entry Point ===
if __name__ == "__main__":
    print("-" * 40)
    print("Day 12: Functions, Return Values, Scope, Inheritance, and JSON\n")
    students = process_students(sample_json)
    # save_file = "day12_students.json"

print("-" * 40)
print("\nReloading students from file to verify...\n")
print("-" * 40)

loaded_students = load_students_from_file(full_path)
for s in loaded_students:
    print(s)
print("-" * 40)
print("\n Program Complete.")
print("-" * 40)