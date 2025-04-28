name = input("Enter your name: ")
program = input("Enter your program (e.g. MSCS): ")
year = int(input("Enter your current year (1 or 2): "))
credits_earned = int(input("Enter the number of credits you have earned so far (out of 32): "))
GPA = float(input("Enter GPA  : "))
working_on_thesis = input("Are you working on a Thesis (yes/ no): ")
part_time_job =  input("Are you working at a part-time job? (yes/ no): ")

print("\nList of available courses: AI Fundamentals, " \
"Machine Learning, Algorithms, Statistics, Discrete Math")

courses_taken = input("Enter your courses taken (comma-separated): ").split(',')
courses_taken = [course.strip() for course in courses_taken]

student = {
    "name": name, 
    "program": program,
    "year": year,
    "courses_taken": courses_taken, 
    "credits_earned": credits_earned, 
    "GPA": GPA, 
    "reserch_interest":"Artificial Intelligence",
    "working_on_thesis": working_on_thesis,
    "part_time_job": part_time_job,   

}
print(f" Loaded Student Profile: {student}")

# Year Check
if student['year'] == 1:
    print("First Year Student, Focus: Foundations!\n")
elif student['year'] == 2:
    print("Second Year Student, Focus: Specialization & Thesis\n")
else:
    print("Unknown Year Status!")

# GPA Check
if student['GPA'] >= 3.5:
    print("GPA Status: Excellent Acamdemic Standing!\n")
elif student['GPA'] < 3.5:
    print("GPA Status: Good Academic Standing\n")
else:
    print("GPA Status: Needs Work!\n")


part_time_job_input = part_time_job == 'yes'
working_on_thesis_input = working_on_thesis == "yes"


# AI Course Progress Check
required_ai_courses = ["AI Fundamentals", "Machine Learning"]
required_math_courses = ["Discrete Math", "Statistics"]
required_algo_courses = ["Algorithms"]
minimum_credits = 32

completed_ai_courses = [course for course in student["courses_taken"] if course in required_ai_courses]
remaining_ai_courses = [course for course in required_ai_courses if course not in student["courses_taken"]]

print(remaining_ai_courses)
if len(required_ai_courses) == len(completed_ai_courses):
    print("AI Essentials: Completed all AI courses.")
else:
    print("AI Essentials:")
    print(f"Completed AI Courses: {completed_ai_courses}")
    print(f"Remaining AI Courses{remaining_ai_courses}")

if remaining_ai_courses == []:
    if student['working_on_thesis']:
        print("Research Track: Thesis option selected.")
        if student["reserch_interest"] == "Artificial Intelligence":
            print("Reserch Focus: Artificial Intelligence")
        else:
            print(f"Reserch Focus: {student['reserch_interest']}")
    else:
        print("Reserch Track, No Thesis Course work only!")


# complete alog and math requirements in program and 
# write a if else for credits remaining, part time job.
# based on remaining clurses, we could put out a graduation timeline in the program, 

print(f"\nStudent: {student['name']}")
print(f"Program: {student['program']}\n")



