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

        print(greet_student(student.name))
        print(f"GPA: {student.gpa}")
        print(f"Grades: {student.grades}")
        print(f"Program: {student.program}")
        print_student_info(student.name, student.gpa)
    return student_objects

# === Save to JSON File ===
def save_students_to_file(students, filename):
    with open(filename, "w") as f:
        json.dump([s.to_dict() for s in students], f, indent=4)
    print(f"Student data saved to {filename}")

# === Load from JSON File ===
def load_students_from_file(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return [Student(d['name'], d['program'], d['grades']) for d in data]

# === Entry Point ===
if __name__ == "__main__":
    print("Day 12: Functions, Return Values, Scope, and JSON\n")
    
    students = process_students(sample_json)

    save_file = "day12_students.json"
    save_students_to_file(students, save_file)

    print("\nReloading students from file to verify...\n")
    loaded_students = load_students_from_file(save_file)

    for s in loaded_students:
        print(s)

    print("\n Program Complete.")
