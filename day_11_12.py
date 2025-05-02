import os
import json

school_name = "Arizona State University."

# function

def greet_student(name):
    # print("Hello, I'm %s, and Im a student at ASU."% (name))
    return "Hello, I'm %s, and Im a student at ASU."% (name)


student = greet_student(name='Justin')
print(student)

def compute_gpa(grades):
    if not grades:
        return 0.0
    return round(sum(grades) / len(grades), 3)

print(compute_gpa([3.5, 4.0, 3.8]))

def is_on_honor_roll(gpa):
    return gpa > 3.7

def print_student_info(name, gpa, school_name):
    department = 'Computer Science'
    print (f"{name} is a student in {department} department, at {school_name}")
    if is_on_honor_roll(gpa):
        print(f"{name} is on the Honor Roll!\n")
    else:
        print(f"{name} is not on the Honor Roll!\n")
    
class Person:
    def __init__(self, name, program):
        self.name = name
        self.program = program
        
    def introduce(self):
        return print(f"Hi I'm {self.name} at ASU and Im in the {self.program} Program.")
     
class Student(Person):
    def __init__(self, name, program, grades):
        super().__init__(name, program)
        self.name = name
        self.program = program
        self.grades = grades
        self.gpa = compute_gpa(grades=grades)
        
    def to_dict(self):
        return {
            "name": self.name, 
            "program":self.program, 
            "grades":self.grades, 
            "GPA":self.gpa, 
        }
    
    def __str__(self):
        return f"{self.name} - {self.program} - GPA: {self.gpa}"

sample_json = '''[
    {"name": "Aditya", "program": "MSCS", "grades": [4.0, 3.8, 3.9]},
    {"name": "Shawn", "program": "MSDS", "grades": [3.5, 3.6, 3.7]},
    {"name": "Drew", "program": "MBA", "grades": [3.2, 3.3, 3.1]}
]'''

def process_student(sample_json):
    student_data = json.loads(sample_json)
    student_objects = []
    for data in student_data:
        student = Student(data['name'], data['program'], data['grades'])
        student_objects.append(student)
        print("-" * 40)
        print(greet_student(student.name))
        print(f'Student Objects >>> {student_objects[0].gpa}')   
        print(f'Student Objects >>> {student_objects[0].grades}')   
        print(f'Student Objects >>> {student_objects[0].name}')   
        print(f'Student Objects >>> {student_objects[0].program}')   

stdnt = process_student(sample_json)        
filename = 'day-12-student-info.json'
current_dir = os.path.dirname(os.path.realpath(__file__))
full_path = os.path.join(current_dir, filename)
print("\nfullpath >>>>>>> \n", full_path)
# got the path that we want to write a file to and we have the filename
# write the python os write code to generate a file with the filename and write 
# student data from the sample_json to the target file

def save_students_to_file():
    try:
        with open(full_path, 'w') as file:
            lst = json.loads(sample_json)
            print(lst)
            string_to_write = json.dumps(lst, indent=4)
            file.write(string_to_write)
    except Exception as e:
        print(f"An Error as occured: {e}")
        
def read_students_from_file(fullpath):
    with open(fullpath, 'r') as file:
        filedata = json.load(file)
        return filedata
                   
save_students_to_file()
student_lst_obj = read_students_from_file(full_path)
for student in student_lst_obj:
    print(student)