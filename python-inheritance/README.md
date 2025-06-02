# Python - Inheritance

This project explores the concept of **inheritance** in Python, focusing on how classes can extend the behavior and structure of other classes. It includes basic inheritance, method overriding, multiple inheritance, and the use of built-in functions such as `type()`, `isinstance()`, `issubclass()` and `super()`.

## 📚 Learning Objectives

By completing this project, you will be able to:

- Define what is a superclass (parent class) and a subclass (child class).
- List all attributes and methods of a class or instance using `dir()`.
- Understand when instances can have new attributes dynamically.
- Implement single and multiple inheritance in Python.
- Override inherited methods and attributes.
- Use `type()`, `isinstance()`, `issubclass()`, and `super()` effectively.
- Understand the purpose and benefits of using inheritance.
- Apply good documentation and coding standards (`pycodestyle`).

---

## 📝 Project Structure

| File | Description |
|------|-------------|
| `0-lookup.py` | Function that returns the list of attributes and methods of an object. |
| `1-my_list.py` | Class `MyList` that inherits from `list` and adds a method to print sorted list. |
| `2-is_same_class.py` | Function that checks if an object is exactly an instance of a given class. |
| `3-is_kind_of_class.py` | Function that checks if an object is an instance of a class or a subclass. |
| `4-inherits_from.py` | Function that checks if an object inherits from a specified class (but is not that class itself). |
| `5-base_geometry.py` | Empty base class `BaseGeometry`. |
| `6-base_geometry.py` | Adds an `area()` method that raises an exception in `BaseGeometry`. |
| `7-base_geometry.py` | Adds `integer_validator()` method to `BaseGeometry`. |
| `8-rectangle.py` | Class `Rectangle` that inherits from `BaseGeometry` and validates `width` and `height`. |
| `9-rectangle.py` | Adds `area()` and `__str__()` methods to `Rectangle`. |
| `10-square.py` | Class `Square` that inherits from `Rectangle` and uses one size argument. |
| `11-square.py` | Adds `area()` and custom `__str__()` to `Square`. |
| `12-square.py` | Same as above but relies entirely on inherited methods. |
| `100-my_int.py` | Advanced: Class `MyInt` that inverts `==` and `!=` operators. |
| `101-add_attribute.py` | Advanced: Function that adds new attribute to object if possible. |

---

## ✅ Requirements

- Python 3.8.5
- Ubuntu 20.04 LTS
- No use of `import` unless explicitly allowed
- Files must be executable
- PEP8 compliant (`pycodestyle 2.7.*`)
- Each module, class, and function must include proper documentation
- Tests (if required) must be placed under a `tests/` folder

---

## 🚀 Usage

To run the individual tasks:

```bash
chmod +x <filename>.py
./<filename>.py


## Author: 
Marivellisse Garcia
