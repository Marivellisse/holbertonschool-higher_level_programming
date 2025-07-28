# Python - Everything is object

## Description

This project explores the core concept that **everything in Python is an object**, including primitive types, collections, functions, and even classes. The project is divided into two sections:

- **Theoretical questions** that test your understanding of object identity, assignment, aliasing, mutability, and memory referencing in Python.
- **Practical scripts** that demonstrate these behaviors in real code scenarios.

This foundational knowledge is critical for understanding how Python works behind the scenes and is commonly tested in technical interviews for Python-related positions.

---

## Background Context

In Python, variables are names that reference objects in memory, not actual containers that store values. This subtle but important behavior explains why changes in one variable might unexpectedly affect another, especially with **mutable types** like lists and dictionaries.

Example:

```python
l = [1, 2, 3]
m = l
l[0] = 'x'
print(m)  # ['x', 2, 3]

Learning Objectives
By the end of this project, you should be able to explain the following:
What is an object
The difference between a class and an instance
Mutable vs immutable objects
What is a reference vs assignment
What is aliasing
How to determine if two variables point to the same object (is)
How to display a variable's identifier using id()
Built-in mutable types: list, dict, set, bytearray
Built-in immutable types: int, float, str, tuple, frozenset, bytes
How Python passes variables to functions (always by object reference)

Requirements
Python Scripts
All files must start with: #!/usr/bin/python3
Files must be executable (chmod +x filename.py)
Interpreted on Ubuntu 20.04 LTS using Python 3.8.5
Must follow pycodestyle (v2.7.*) formatting
All files must end with a new line
File lengths will be checked using wc
.txt Answer Files
One line only
No shebang (#!/usr/bin/python3)
Must end with a new line

Author Marivellisse Garcia
