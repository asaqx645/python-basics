# 🐍 Python Programming Curriculum – Day 1 to Day 30

Welcome to the **Python 13-Day Programming Curriculum** – a hands-on learning journey designed for beginners and intermediate learners. Each day builds on the last with increasing complexity, culminating in a strong foundation of programming fundamentals using Python 3.

---

## 📘 Curriculum Overview

Each lesson includes:

* Python script (`.py`) files
* Interactive coding tasks
* Real-world examples
* JSON usage, classes, functions, and more

---

## 📅 Daily Breakdown

###  Day 1: Python Setup & Hello World

* Installing Python
* Writing and running your first program
* `print()` and `# comments`

###  Day 2: Variables and Data Types

* `int`, `float`, `str`, `bool`
* Type checking with `type()`
* Naming conventions

###  Day 3: Input & String Formatting

* Using `input()`
* String interpolation: `%s`, `format()`, and f-strings

###  Day 4: Conditional Statements

* `if`, `elif`, `else`
* Comparison operators
* Truthiness

###  Day 5: Loops

* `for` and `while` loops
* `break` and `continue`
* Loop over strings and lists

###  Day 6: Lists

* Creating and modifying lists
* Indexing and slicing
* Using `append()`, `remove()`, `sort()`

###  Day 7: Tuples and Dictionaries

* Tuples: immutable lists
* Dictionaries: key-value storage
* Accessing, adding, and modifying entries

###  Day 8: Nested Structures

* List of dictionaries
* Looping through nested data
* Conditional logic inside loops

###  Day 9: Advanced Looping with Lists

* Iterating over complex structures
* Modifying lists inside loops
* Combining and splitting lists

###  Day 10: Functions – Introduction

* Defining and calling functions
* Parameters and arguments
* Return values
* Scope: local vs global

###  Day 11: Classes & JSON I

* Defining a class with `__init__()`
* Attributes and methods
* Basic JSON serialization using `json.dumps()` and `json.loads()`

###  Day 12: Inheritance and Class Composition

* Base `Person` class
* `Student` subclass with `super()`
* Object conversion with `.to_dict()`
* Saving and loading student data using files

###  Day 13: Functions II – Default Arguments, \*args, \*\*kwargs, and Lambda

* Default argument values
* Flexible function calls using `*args` and `**kwargs`
* Anonymous functions with `lambda`
* Real-world examples with `sorted()` and `key=lambda`

###  Day 14: Functional Programming – map(), filter(), reduce()
* Understanding higher-order functions
* Applying map() to transform sequences
* Using filter() to select items from sequences
* Leveraging reduce() to accumulate results
* Introduction to functools.reduce
* Using lambda with functional constructs
* Comparing functional vs loop-based approaches


---

## ⚙️ Project Setup Instructions

### 1. 📦 Create and Activate a Virtual Environment

```bash
# Step 1: Create the virtual environment
python -m venv venv

# Step 2: Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. 🧪 Install Required Packages (if any)

```bash
pip install -r requirements.txt
```

> *Note: Currently, no external libraries are used. This is a pure Python curriculum.*

---

## 🧠 Recommended VS Code Configuration

### 📁 `.vscode/launch.json`

To enable F5 to run the current Python file:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

> 💡 Create a `.vscode` folder at the root of your project and save the above as `launch.json`.

---

## 📂 Project Structure

```
├── day_01.py                  # Intro to Python and print statements
├── day_02.py                  # Variables and basic types
├── day_03.py                  # Input and string formatting
├── day_04.py                  # Conditional statements
├── day_05.py                  # Loops and iteration
├── day_06.py                  # Lists
├── day_07.py                  # Tuples and dictionaries
├── day_08_09.py               # Nested structures and advanced list operations
├── day_10.py                  # Introduction to functions
├── day_11_12.py               # Classes, inheritance, and JSON
├── day-12-student-info.json   # Sample student data output file
├── day_13.py                  # Advanced functions: *args, **kwargs, lambda
├── .vscode/
│   └── launch.json            # VS Code debugging configuration
├── README.md                  # This file
```

---

## 🧑‍🏫 Author

**Aditya Singh Sandhu**
Educator | Software Engineer | Python Instructor
