import json



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
    
class Student:
    def __init__(self, name, program, grades):
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
    
    # def __str__(self):
    #     return f"{self.name} - {self.program} - GPA: {self.gpa}"

student_cls= Student("Shawn", "MScCS", [3.5, 4.0, 3.8])
print(student_cls.to_dict())



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
        print(greet_student(student.name))
        print(f'Student Objects >>> {student_objects[0].gpa}')   
        print(f'Student Objects >>> {student_objects[0].grades}')   
        print(f'Student Objects >>> {student_objects[0].name}')   
        print(f'Student Objects >>> {student_objects[0].program}')   
stdnt = process_student(sample_json)        