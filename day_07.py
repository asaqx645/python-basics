# -----------------------------
# Expanded Mini Project: Contact Book
# -----------------------------
print("Welcome to the Contact Book")
contacts = {} # instanctiates a dict object 

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added {name} and {phone} to contacts")

def search_contact(name):
    if name in contacts:
        print(f"Contact Found: {name}")
    else:
        print(f"{name}Not Found in contacts")

def remove_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted from contacts")
    else:
        print(f"{name} was not found in contacts")

def update_contact(name, newphone):   
    if name in contacts:
        contacts[name] = newphone
        print(f"{name} added to contacts along with {newphone}.")
    else:
        print(f"{name} was not found in contacts")

def list_contacts(name):
    if name in contacts:
        print(f"{name} was found in contacts")
        for name, phone in contacts.items():
            print(f"{name} & {phone}")
    else:
        print(f"{name} not found.")

# add_contact("Alice", "555-1234")
# add_contact("Bob1", "555-5678")
# add_contact("Bob2", "555-5678")
# list_contacts("Bob2")
# list_contacts("Bob4")

print("\nQuiz Time!")

# Variables
x = 10
y = 20
z = x + y
print(f"What is z? {z}") # 30


# Types
text = "Hello" # string
number = 123 # integer
decimal = 3.14 # float or decimal in math
is_valid = True # boolean
# if you are not sure on the type of data use the inbuilt type() function in python 

print("Type of text:", type(text))       # str
print("Type of number:", type(number))   # int
print("Type of decimal:", type(decimal)) # float
print("Type of is_valid:", type(is_valid)) # bool


# Collections
fruits = ["apple", "banana", "cherry"]
print("Second fruit:", fruits[0])  # "apple"

user_info = {"name": "John", "age": 25} # you can access 
# dictionaries that use hash maps under the hood by keys
print("User's name:", user_info["name"])  
print("User's age:", user_info["age"]) 

unique_ids = {1, 2, 3, 3, 6, 6 , 6, 5, 2, }
print("Unique IDs:", unique_ids)  # Unique IDs: {1, 2, 3, 5, 6}