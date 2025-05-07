import os
import datetime
import random

# === Setup: Ensure the output folder exists ===
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, "output")
os.makedirs(output_dir, exist_ok=True)

file_path = os.path.join(output_dir, "day15_data.txt")

# === Step 1: Write Header and One Line Using .write() ===
with open(file_path, "w") as f:
    f.write("=== Day 15: File I/O in Python ===\n")
    f.write("This file demonstrates write(), writelines(), and appending.\n\n")

# === Step 2: Generate Data and Write Using .writelines() ===
students = ["Aditya", "Shawn", "Drew", "Alice", "Bob"]
programs = ["MSCS", "MSDS", "MBA"]
lines = ["Name\tProgram\tScore\tTimestamp\n"]

for _ in range(10):
    name = random.choice(students)
    program = random.choice(programs)
    score = round(random.uniform(2.0, 4.0), 2)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines.append(f"{name}\t{program}\t{score}\t{timestamp}\n")

with open(file_path, "a") as f:  # Append using writelines()
    f.writelines(lines)

# === Step 3: Append Using Formatted String + write() ===
with open(file_path, "a") as f:
    f.write("\nAdditional Scores (write with format):\n")
    for _ in range(5):
        name = random.choice(students)
        score = random.randint(50, 100)
        f.write("Student: {:<8} | Score: {}\n".format(name, score))

# === Step 4: Read Entire Content with .read() ===
with open(file_path, "r") as f:
    content = f.read()

print("\n--- FILE CONTENT ---")
print(content)

# === Step 5: Reading line-by-line with .readlines() ===
print("\n--- FIRST 5 LINES USING .readlines() ---")
with open(file_path, "r") as f:
    lines = f.readlines()
    for i in range(min(5, len(lines))):
        print(lines[i], end="")

# === Step 6: Read first line with .readline() ===
print("\n--- FIRST LINE USING .readline() ---")
with open(file_path, "r") as f:
    first_line = f.readline()
    print(first_line)
