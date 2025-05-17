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

###  Day 15: File I/O Operations
* w write mode (overwrite)
* a append mode (adds to the end)
* r read mode (view contents)
* r+ read + write mode (edit without deleting)

###  Day 16: File I/O Operations (Part 2)
* readlines()
* readline()
* writelines()
* modules - datetime(), random()

###  Day 17: - Modules and Imports
* ramdom(), math() modules
* Import Custom Python Module
* docstring __doc__ method 

###  Day 18: - Intro to Json()
* json() module
* data type - dict
* build million line 100000 dictionaries .json file

### Day 19
* built in functions
* len(), min(), max()
* sum(), sorted(), enumerate()
* help(), round()

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
(pybasics-venv) @asaqx645 ➜ /workspaces/python-basics (main) $ tree
.
├── LICENSE
├── README.md
├── __pycache__
│   └── helpers.cpython-312.pyc
├── daily_folder
├── day-12-student-info.json
├── day_01.py
├── day_02.py
├── day_03.py
├── day_04.py
├── day_05.py
├── day_06.py
├── day_07.py
├── day_08_09.py
├── day_10.py
├── day_11_12.py
├── day_13.py
├── day_14.py
├── day_15.py
├── day_16.py
├── day_17.py
├── helpers.py
└── output
    └── day15-data-part-2.txt
```

---

## 🧑‍🏫 Author

**Aditya Singh Sandhu**
Educator | Software Engineer | Python Instructor
