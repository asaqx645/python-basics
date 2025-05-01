# Part 1 
# this is the file for day 9 loops break and continue lists specific
# my_list = [1, 2, 3, 4, 5, 6]
# print("Original List: ", my_list)
# print(len(my_list))
# print(type(my_list[0]))
# print("beginning to the end: ", my_list[0:]) # beginning to the end
# print("beginning to the end: ", my_list[:]) # beginning to the end
# print("print nothing: ", my_list[:0]) # print nothing
# print("print everything: ", my_list[:5]) # print everything

# my_list_string = ["Is this is a string type?"] # an index 
# # is an accessor of a list data type. 
# print("String List: ", my_list_string)
# print(len(my_list_string))
# print(type(my_list_string))
# print(type(my_list_string[0]))

# new_lst = my_list + my_list_string
# print("new list: ", new_lst)
# print("length of new list: ", len(new_lst))
# my_list[3] = int(684654687984654)
# print("what is the new value of my_list[3]: ", my_list[3])
# print(my_list)

# print(my_list_string)
# print(new_lst + ["lakesrj1203984"])
# my_list[2]=9
# print(len(my_list))
# my_list[5] = 155

# print(my_list)
# # Part 2
# important_courses = ["AI Fundamentals","Machine Learning", "Algorithms", "Statistics", "Discrete Math"]
# courses_taken = ["AI Fundamentals", "Algorithms", "Statistics" ]

# for subject in courses_taken:
#     print("Subjects Taken: ", subject)
    
# for courses in important_courses:
#     print(f"Important Course: {courses}")
    
# for course in important_courses:
#     if course not in courses_taken:
#         print("Missing: ", course)
#     else:
#         print("Found: ", course)
        
        
# for course in important_courses:
#     if course not in courses_taken:
#         print(f"Missing: {course} so breaking the loop!")
#         break
#     if course == 'Statistics':
#         print(f"Skipping extra checked after {course}")
#         continue
#     print("Processed: ", course)
    
student_name = "TommyWalters"
for char in student_name:
    # print("Aplhabet In String: {}".format(char))
    print("Aplhabet In String: %s" % (char)) # %d and for float %.2f
    
# for number in my_list:
#     print("Number in My List is : %d" % (number))   
    
print("\nGenerating two-letter .com domain names")    
letter1= 'a'
letter2 = '?'

while letter1 <= 'z':
    letter2 = 'a'
    while letter2 <= 'z':
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1) #  Converts letter2 to its ASCII value,
        # increments it by 1, and converts it back to a character.
    letter1 = chr(ord(letter1) + 1)  #  Converts letter1 to its ASCII value, 
    # increments it by 1, and converts it back to a character.