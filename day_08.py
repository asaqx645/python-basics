name = input("Enter your name: ")
program = input("Enter your program (e.g. MSCS): ")
year = int(input("Enter your current year (1 or 2): "))
credits_earned = int(input("Enter the number of " \
"credits you have earned so far (out of 36): "))
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
required_ai_courses = ["AI Fundamentals", "Machine Learning"] # 2
required_math_courses = ["Discrete Math", "Statistics"] # 2
required_algo_courses = ["Algorithms"] # 1
minimum_credits = 36

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


# credits
if student['credits_earned'] >= minimum_credits:
    print("Credit Status: Eligible to Graduate.\n")
else:
    credits_remaining = minimum_credits - student['credits_earned']
    print(f"Current Credit Status: {credits_remaining}, "\
          "so more credits are needed to graduate.")

# math requirements
completed_math_courses = [course for course in student['courses_taken']
                          if course in required_math_courses]
remaining_math_courses = [course for course in student['courses_taken']
                          if course not in student['courses_taken']]
print("completed_math_courses & remaining_math_courses: ", 
      completed_math_courses, remaining_math_courses)

if len(completed_math_courses) == 2:
    print("Math Essentials: Completed all Math courses.\n")
else:
    print("Math Essentials: ")
    print(f"Completed :{completed_math_courses}")
    print(f"Remaining :{remaining_math_courses}")
# complete algo
completed_algo_courses = [course for course in student['courses_taken']
                          if course in required_algo_courses]
                          
remaining_algo_courses = [course for course in student['courses_taken']
                          if course not in student['courses_taken']]
if len(completed_algo_courses) == len(required_algo_courses):
    print("Algorithm Essentials: Completed all Algorithm Courses. \n")
else:
    print("Algorithm Essentials: ")
    print(f"Completed :{completed_algo_courses}")
    print(f"Remaining :{remaining_algo_courses}")


print(f"\nStudent: {student['name']}\n")
print(f"Program: {student['program']}\n")

# write a if else for  remaining, part time job.
if part_time_job_input is True:
    print(f"Yes, Student {student['name']} is working a part time job.\n")
    if GPA >= 3.5 and len(student['courses_taken']) >= 3:
        print("Impressive! Maintaining Strong Academic Performace" \
        ", taking multiple courses, while holding a job\n")
    elif GPA < 3.0:
        print("Warning! Part time work might be affecting your grades, consider" \
        "taking fewer courses\n")
    else:
        print("Doing Well balancing work and study!\n")
else:
    print(f"No, Student {student['name']} is full time and "\
          "not working a part time job.\n")
    
# based on remaining courses, we could put out a graduation 
if student['credits_earned'] >= 28:
    print("Projected Graduation Timeline: Within 1 semester\n")
elif student['credits_earned'] <=18:
    print("Projected Graduation Timeline: Within 2 semester.\n")
else:
    print("Projected Graduation Timeline: 1 year or more\n")

# Fix the output of the if elif else around math, since the 
# remaining math course is Discrete math.