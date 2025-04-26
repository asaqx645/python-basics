# # ----------------------------------
# # LISTS – Nested and Dually Nested
# # ----------------------------------
# shopping_list = ["milk", "bread", "eggs"]
# data_1 = ["judy", 654, 123.987, ['ny', '50480', 'sdf65g4sdf65f4gh65sef']]
# print(data_1)
#  # nested list access
# var1 = data_1[0]
# lst = data_1[3][2]
# # lst = data_1[3][1]
# print(f"var1 >>> {var1}")
# print(f"lst >>> {lst}")


# weekly_menu = [
#     ["pasta", "salad"],      # 0
#     ["sandwich", "chips"],   # 1
#     ["curry", "rice"]        # 2
# ]
# print("Weekly menu (nested list):", weekly_menu)
# print("Tuesday's lunch:", weekly_menu[1][1])  #chips

# student_courses = [
#     ["Alice", ["Math", "Physics"]],
#     ["Bob", ["History", "English"]],
#     ["Carol", ["Art", "Biology"]]
# ]
# print("student_courses: ", student_courses)
# print(f"Carol's first course >>> {student_courses[2][1][0]}")

# # ----------------------------------
# # TUPLES – Nested and Immutable
# # ----------------------------------

# coordinates = (40.7128, -74.0060)
# print("Simple tuple (coordinates):", coordinates)
# print("Simple tuple (coordinates):", coordinates[0])

# points = ((1, 2), (3, 4), (5, 6))
# print("Points (nested tuple):", points)
# print("Second point x value:", points[1][0]) # 3


# ----------------------------------
# DICTIONARIES – Nested and Dually Nested
# ----------------------------------

# user = {
#     "dict1": 
#     {"username": "jsmith","email": "jsmith@outlook.com"},
#     "dict2":
#     {"username": "avi", "email": "avi@gmail.com"},
#     }

# print(user)
# print("get to the first dictionary:", user['dict1'])
# print("get to the second dictionary:", user['dict2'])
# print("username of the first dictionary:", user['dict1']['username'])

# employee = {
#     "name": "John Doe",
#     "contact": {
#         "email": "john@example.com",
#         "phone": ["555-1234", "203-731-1689"]
#     },
#     "skills": ["Python", "SQL"]
# }
# print("employee's first skill is: ", employee['skills'][0])
# print("employee's second skill is: ",employee['skills'][1])

# company = {
#     "Engineering": {
#         "Backend": ["Alice", "Bob"],
#         "Frontend": ["Carol", "Dave"]
#     },
#     "HR": {
#         "Recruiters": ["Eve", "Frank"]
#     }
# }

# obj_1 = company['HR']['Recruiters'][1]
# # obj_1 = company['HR']['recruiters'][1]
# print(f"2nd hr recruiters name is: {obj_1}")


# ----------------------------------
# SETS – Unique and Set Operations
# ----------------------------------

simple_set = {1, 2, 2, 3, 4}

simple_set = {1, 2, 2, 3, 4}
print("Set with duplicates removed:", simple_set)
print(len(simple_set))

set_a = {1, 2, 3, 3, 3, 3}
set_b = {3, 4, 5}
print("Union:", set_a | set_b)

print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b) # cover in day 7 and then move on to topic 4/25/2025

student_courses =(
   ("Alice",("Math", "Physics")),
   ("Bob",("History", "English")),
   ("Carol",("Art", "Biology"))
)
print("student_courses: ", student_courses)
print(f"Carol's first course >>> {student_courses[2][1][0]}")