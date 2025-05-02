# === Day 13: Functions II - Default Args, *args, **kwargs, Lambda ===

# --- Default Argument Example ---
def welcome(name="Student"):
    return f"Welcome to Python Day 13, {name}!"

print(welcome())
print(welcome("Aditya"))

# --- *args Example ---
def print_courses(*courses):
    print("Enrolled in the following courses:")
    for course in courses:
        print(f"- {course}")

print_courses("AI", "Statistics", "Python")

# --- **kwargs Example ---
def display_profile(**kwargs):
    print("Student Profile:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_profile(name="Shawn", program="MSDS", year=2)

# --- Using *args with a sum calculator ---
def total_credits(*credits):
    return sum(credits)

print("Total Credits:", total_credits(3, 4, 3, 2))

# --- Using **kwargs with a filter ---
def filter_gpa(**students):
    print("Honor Roll Students:")
    for name, gpa in students.items():
        if gpa >= 3.7:
            print(f"{name}: {gpa}")

filter_gpa(Aditya=3.9, Shawn=3.6, Drew=3.2)

# --- Lambda Function for Quick GPA Scale ---
gpa_scale = lambda gpa: "Excellent" if gpa >= 3.7 else "Needs Work"
print("Aditya's GPA status:", gpa_scale(3.9))
print("Drew's GPA status:", gpa_scale(3.2))
