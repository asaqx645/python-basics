import os
import random
import datetime

current_working_dir = os.getcwd()
current_dir = os.path.dirname(os.path.abspath(__file__))
print("current_working_dir: ", current_working_dir)
print("current_dir: ", current_dir)
output_path = os.path.join(current_dir, 'output')
os.makedirs(output_path, exist_ok=True)
file_path = os.path.join(output_path, 'day15-data-part-2.txt')
print(file_path)

with open(file_path, 'w') as out_file:
    out_file.write("Line 1: Day 16 Part 2 - This file demonstrates File I/O in Python.\n")
    out_file.write("Line 2: This line and above was writtin in w write mode.\n")
    out_file.write("Line 3: This file will have the readline(), readlines() random and datetime Functions.\n")
    
students = ["Aditya", "Sean", "Jason", "Michelle", "John"]
programs = ["AIML", "MSCS", "MENG", "EENG"]
lines = ["Name\tProgram\tScore\tTimestamp\n"]

for _ in range(10):
    name = random.choice(students)
    program = random.choice(programs)
    score = round(random.uniform(2.0, 4.0), 2)
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    lines.append(f"{name}\t{program}\t{score}\t{timestamp}\n")
    
print("lines: ", lines)

with open(file_path, 'a') as file:
    write_lines = file.writelines(lines) # double check if a writelines does inface 
    # append to end of line or overwrites the contnets of the txt file. 
    
    