import os
current_working_dir = os.getcwd()
current_dir = os.path.dirname(os.path.abspath(__file__))
print("current_working_dir: ", current_working_dir)
print("current_dir: ", current_dir)
output_path = os.path.join(current_dir, 'output')
os.makedirs(output_path, exist_ok=True)
file_path = os.path.join(output_path, 'day15-data.txt')
print(file_path)

with open(file_path, 'w') as out_file:
    out_file.write("Line 1: This file demonstrates File I/O in Python.\n")
    out_file.write("Line 2: This line and above was writtin in w write mode.\n")
    
with open(file_path, 'a') as out_file:
        out_file.write("Line 3: This line and above was writtin in a write mode.\n")
    
with open(file_path, 'r') as out_file:
   data = out_file.read()
   print("data:", data)
    
print("======Using r+ Mode======")
with open(file_path, 'r+') as out_file:
    out_file.seek(0)
    out_file.write("Line 0: Updated Using the a mode.\n")
    out_file.write("Line 1: This file demonstrates File I/O in Python.\n")
    out_file.write("Line 2: This line and above was writtin in w write mode.\n")
    out_file.truncate()
    # out_file.write("Line 0.5: More Lines Updated Using the r+ mode.\n")
    out_file.seek(0)
    print(out_file.read())
    
with open(file_path, 'a') as out_file:
        out_file.write("Line 3: This line and above was writtin in a write mode.\n")

with open(file_path, 'r') as out_file:
   data = out_file.read()
   print("data: \n", data)