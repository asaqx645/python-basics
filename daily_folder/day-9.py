# Day 10 - Python Basics: Lists, Loops, break, continue, Nested Loops

# === PART 1: Basic List Operations ===
# Introduce lists: How to create, access, modify, slice, and delete elements.

my_list = [1, 2, 3]
print("Original list:", my_list)

my_list = list('123')  # Convert string into a list of characters
print("Using list('123'):", my_list)

my_list = [1, 2, 3]
print("Access element at index 1:", my_list[1])  # Remember, indexing starts at 0

print("Slicing [1:3]:", my_list[1:3])  # Slicing returns a new sublist from index 1 to 2

my_list = [1, 2] + [3]
print("List addition:", my_list)  # Lists can be combined with +

my_list[2] = 9
print("Changing value at index 2:", my_list)  # Change element by index

my_list[len(my_list):] = [9]
print("Appending using slice:", my_list)  # Appending using slice syntax (alternative to append)

del my_list[1]
print("Deleting index 1:", my_list)  # Delete the element at index 1

# End of Part 1:
# Now the student knows how to create, read, update, and delete items from a list.

# === PART 2: Looping Over Lists ===
# Show how to loop through lists and check membership.

courses_taken = ["AI Fundamentals", "Statistics", "Algorithms"]
important_courses = ["AI Fundamentals", "Machine Learning", "Algorithms", "Statistics", "Discrete Math"]

print("\nLooping through completed courses:")
for course in courses_taken:
    print("Completed:", course)

print("\nLooping through important courses:")
for course in important_courses:
    if course not in courses_taken:
        print("Missing:", course)
    else:
        print("Found:", course)

# End of Part 2:
# The student now understands how to traverse lists and check conditions inside loops.

# === PART 3: break and continue ===
# Teach breaking out of a loop early and skipping certain iterations.

for course in important_courses:
    if course not in courses_taken:
        print("Breaking loop at missing:", course)
        break  # Stop checking once we find a missing course
    if course == "Statistics":
        print("Skipping extra checks after:", course)
        continue  # Skip further processing for Statistics
    print("Processed:", course)

# End of Part 3:
# Students now understand that break exits the loop immediately and continue skips to next iteration.

# === PART 4: Looping Over a String ===
# Strings are sequences. We can loop over each character just like a list.

student_name = "Aditya"
print("\nLooping over student's name:")
for char in student_name:
    print(f"Letter: {char}")

# End of Part 4:
# Now the student sees that strings can be looped over, one character at a time.

# === PART 5: Nested Loops - Drawing a Face ===
# Introduction to nested loops: A loop inside another loop.
# In this case, drawing a simple face.

nose = '0'
user_value = '-'

# (This interactive section is skipped during code walkthrough.)
# Uncomment below if teaching live to show input control inside loops.

# while user_value != 'q':
#     print(' {} {} '.format(user_value, user_value))  # Print eyes
#     print('  {}  '.format(nose))                    # Print nose
#     print(user_value * 5)                           # Print mouth
#     print('\n')
#     user_input = input("Enter a character ('q' to quit): \n")
#     user_value = user_input[0]

print("Face drawing simulation skipped for static script.")

# End of Part 5:
# Students are introduced to controlling output formatting with nested loops and user input.

# === PART 6: Real World Example - Empanadas and Tacos (break) ===
# Find the first meal combination that uses all the user's money exactly.

empanada_cost = 3
taco_cost = 4

user_money_input = input("\nEnter money for meal (example 20 or 31): ")
user_money = int(user_money_input)

# Maximum numbers we might buy
max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

# Important: we use range(max_tacos + 1) because range() is exclusive of the last value.
# Without +1, we'd miss testing the maximum number itself.

meal_cost = 0

for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):
        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)
        if meal_cost == user_money:
            break  # Found a matching combination, break inner loop
    if meal_cost == user_money:
        break  # Also break outer loop if found

if meal_cost == user_money:
    print('${} buys {} empanadas and {} tacos without change.'
          .format(meal_cost, num_empanadas, num_tacos))
else:
    print('You cannot buy a meal without having change left over.')

# End of Part 6:
# Students understand how nested loops + break find the first acceptable solution.

# === PART 7: Real World Example - Continue (Dividing Meals Among Diners) ===
# Find all meal combinations where food divides evenly among all diners.

empanada_cost = 3
taco_cost = 4

user_money = int(input("\nEnter money for meal: "))
num_diners = int(input("How many people are eating: "))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
num_options = 0

for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):
        # Check if total items are divisible by diners
        if (num_tacos + num_empanadas) % num_diners != 0:
            continue  # Skip invalid divisions
        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)
        if meal_cost == user_money:
            print('${} buys {} empanadas and {} tacos without change.'
                  .format(meal_cost, num_empanadas, num_tacos))
            num_options += 1

if num_options == 0:
    print('You cannot buy a meal without having change left over.')

# End of Part 7:
# Students now see how continue can filter out bad options and allow all good matches.

# === PART 8: Nested Loops - Generating Two-Letter Domain Names ===
# Use nested loops to create every possible two-letter domain name from a-z.

print("\nGenerating two-letter .com domain names:")

letter1 = 'a'
letter2 = '?'

while letter1 <= 'z':  # Outer loop over first letter
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop over second letter
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1)  # Move to next letter
    letter1 = chr(ord(letter1) + 1)  # Move outer loop to next letter

# End of Part 8:
# Students learn that combining loops can generate every possible combination of characters.

# === End of Day 10 ===
print("="*50)
print("End of Day 10 Lesson: Lists, Loops, break, continue, real-world examples")
print("Up next: Day 11 - Looping over dictionaries, functions, and more!")
