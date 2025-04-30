import json

# === Part 1: Basic Function to Greet a Student ===
def greet_student(name):
    return f"Hello, {name}! Welcome to Python Day 11."

# === Part 2: Compute GPA from a list of grades ===
def compute_gpa(grades):
    if not grades:
        return 0.0
    return round(sum(grades) / len(grades), 2)

# === Part 3: Student class to encapsulate data and behavior ===
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

# === Part 4: Sample student data in JSON format ===
sample_json = '''
[
    {
        "name": "Aditya",
        "program": "MSCS",
        "grades": [4.0, 3.8, 3.9]
    },
    {
        "name": "Shawn",
        "program": "MSDS",
        "grades": [3.5, 3.6, 3.7]
    },
    {
        "name": "Drew",
        "program": "MBA",
        "grades": [3.2, 3.3, 3.1]
    }
]
'''

# === Part 5: Load JSON data and process students ===
def process_students(json_data):
    students_data = json.loads(json_data)
    student_objects = []

    for data in students_data:
        student = Student(data['name'], data['program'], data['grades'])
        student_objects.append(student)
        print(greet_student(student.name))
        print(student)
        print("-" * 40)

    return student_objects

# === Part 6: Save students to JSON file ===
def save_students_to_file(students, filename):
    with open(filename, "w") as f:
        json.dump([s.to_dict() for s in students], f, indent=4)
    print(f"Student data saved to {filename}")

# === Part 7: Load students from file ===
def load_students_from_file(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return [Student(d['name'], d['program'], d['grades']) for d in data]

# === Entry Point ===
if __name__ == "__main__":
    print("Starting Day 11 Python Program...\n")
    
    students = process_students(sample_json)
    
    save_file = "day11_students.json"
    save_students_to_file(students, save_file)
    
    print("\nReloading students from file to verify...\n")
    loaded_students = load_students_from_file(save_file)

    for s in loaded_students:
        print(s)
    
    print("\nProgram complete. Functions, JSON, and Classes used.")
