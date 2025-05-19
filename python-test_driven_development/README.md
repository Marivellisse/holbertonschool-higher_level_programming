# Python - Test Driven Development (TDD)

## 📚 Description
This project is part of the Holberton School curriculum and focuses on applying **Test Driven Development (TDD)** in Python. You will learn how to write functions and document them using `doctest` and `unittest`, ensuring correctness by covering various edge cases.

---

## 🎯 Learning Objectives

By the end of this project, you will be able to:

- Understand the importance of testing in Python
- Write functions using TDD methodology
- Use `doctest` to write embedded tests in docstrings
- Write proper documentation for modules and functions
- Handle edge cases and raise appropriate exceptions
- Create and run unit tests using the `unittest` module

---

## 🧪 Requirements

### Python Scripts
- All code uses Python 3.8.5 and runs on Ubuntu 20.04 LTS
- Files must end with a new line and start with `#!/usr/bin/python3`
- Must follow `pycodestyle` version 2.7.\*
- All scripts must be executable

### Python Test Cases
- Tests are stored in the `tests/` directory
- Test files use `.txt` for `doctest`, `.py` for `unittest`
- Run with:
  - `python3 -m doctest ./tests/*`
  - `python3 -m unittest tests.test_filename`

---

## 📂 Project Structure


---

## ✅ Function Overview

### 0. `add_integer(a, b=98)`
Adds two integers or floats. Raises `TypeError` if inputs are not numeric.

### 1. `matrix_divided(matrix, div)`
Divides all elements in a matrix by a number. Rounds to 2 decimals. Raises `TypeError` or `ZeroDivisionError` as needed.

### 2. `say_my_name(first_name, last_name="")`
Prints "My name is <first name> <last name>". Validates that names are strings.

### 3. `print_square(size)`
Prints a square using `#` character. Validates `size` is a non-negative integer.

### 4. `text_indentation(text)`
Prints text with two newlines after `.`, `?`, and `:`. Strips extra spaces.

### 5. `max_integer(list=[])`
Finds and returns the max integer in a list. Returns `None` if the list is empty.

---

## 👨‍💻 Author

Marivellisse Garcia  
Holberton School - Software Engineering Program

---

## 📜 License

This project is part of Holberton School’s curriculum and is intended for educational use only.

