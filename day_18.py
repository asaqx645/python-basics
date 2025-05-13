import json
import random
import time
import os

current_working_dir = os.getcwd()
print(current_working_dir)
output_path = os.path.join(current_working_dir, 'output')
os.makedirs(output_path, exist_ok=True)
file_path = os.path.join(output_path, 'day18-student-data.json')
print(file_path)

def generate_students(num_students=1000000):
    students = [] # list data type
    for i in range(num_students):
        student = {
            "id": i+1 , 
            "name": f"Student_{i+1}", 
            "program": random.choice(["MSCS", "AIML", "MSCSC", "CSC"]),
            "grades": [round(random.uniform(2.0, 4.0), 2)
                       for gpa in range(3)],
            "graduated": random.choice([True, False]) 
        }
        students.append(student)
    return students

print("Generated 100000 students")
start_time = time.time()
print(start_time) 
students_ = generate_students()

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(students_, file, indent=4)

print("File written to OUTPUT Folder!")