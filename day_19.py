import os
import json

languages = ['swift', 'c++', 'go', 'javascript', 'c#']
print('list of languages: ', languages)
print('length of languages: ', len(languages))
print('min of languages: ', min(languages)) # use for integers over strings 
print('max of languages: ', max(languages)) # use for integers over strings
print('------------')
l1 = []
for char in languages[0]:
    print(ord(char))
    l1.append((ord(char)))
print('------------')    
print(sum(l1))
print('------------')

l2 = []
for char in languages[4]:
    l2.append((ord(char)))
print(sum(l2))
print('------------')

l3 = []
for char in languages[3]:
    print(ord(char))
    l3.append((ord(char)))
print('------------')
print(sum(l3))
print('------------')

nums = [12,34,456,78,54,98,43,65432,123,987,98987,54387,7432]
print("this is the max of the nums list :", max(nums))
print("this is the min of the nums list :", min(nums))
print("this is the sum of the nums list :", sum(nums))
print("this is the sorted of the nums list :", sorted(nums))
len_nums = len(nums)
key = int(input ("enter a integer from these option's [12,34,456,78,54,98,43,65432,123,987,98987,54387,7432]:\n"))

def linear_search(nums, len_nums, key):
    """This is the linear Search Function in Python 3.12.1

    Args:
        nums (list): is a list data type that holds ints for computation
        len_nums (int): it is the size of the nums global list 
        key (int): integer, ie whole number should be chosen
        and from the list on the console

    Returns:
        int: 1 means that the key was found, and 
        -1 means that the key was not found.
    """
    for i in range(len_nums):
        if nums[i] == key:
            return 1
    return -1

key_index = linear_search(nums, len_nums, key)

if key_index == 1:
    print(f"{key} was found")
else:
    print(f"{key} was not found")
    
print(f"This is the DOCSTRING: \n{help(linear_search)}")

getcwd = os.getcwd()
print(getcwd)
file = os.path.join(getcwd, 'day-12-student-info.json')
print(file)


with open(file, 'r') as dayfile:
    lst1 = dayfile.readlines()
    json_string = ''.join(lst1)
    print((json_string))
    loadobj = json.loads(json_string)
    
    for key, value in enumerate(loadobj):
        name = value["name"]
        program = value["program"]
        gpa = round(sum(value["grades"]) / len(value["grades"]), 2)
        print(f"{key}: {name} - {program} - GPA: {gpa}")
# print(students)