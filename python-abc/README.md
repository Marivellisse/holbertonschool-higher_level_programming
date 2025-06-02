# Python - Abstract Classes and Interfaces

This project explores advanced concepts in **Object-Oriented Programming (OOP)** using Python, with a focus on **abstract base classes (ABCs)**, **interfaces**, **duck typing**, **method overriding**, **mixins**, and **multiple inheritance**.

It reinforces Python's flexible and powerful type system through practical and conceptual exercises.

---

## 📚 Learning Objectives

By completing this project, you will be able to:

- Define and use **abstract base classes** with the `abc` module.
- Apply **interfaces** and implement **duck typing** to write flexible code.
- Override built-in methods like `__next__()` and use `super()` effectively.
- Compose behaviors using **mixins**.
- Handle **multiple inheritance** and understand **method resolution order (MRO)**.
- Subclass and extend Python’s built-in types (e.g., `list`, `iterator`).

---

## 📂 Project Structure

| File                      | Description |
|---------------------------|-------------|
| `task_00_abc.py`          | Defines abstract class `Animal` with subclasses `Dog` and `Cat` implementing `sound()` |
| `task_01_duck_typing.py`  | Abstract class `Shape` with `Circle` and `Rectangle` subclasses; includes `shape_info()` function using duck typing |
| `task_02_verboselist.py`  | Extends the `list` class as `VerboseList` to print messages when modified |
| `task_03_countediterator.py` | Custom iterator `CountedIterator` that counts how many times `__next__()` has been called |
| `task_04_flyingfish.py`   | Class `FlyingFish` inherits from both `Fish` and `Bird` and overrides `swim`, `fly`, and `habitat` methods |
| `task_05_dragon.py`       | Demonstrates mixins: `SwimMixin`, `FlyMixin`, and a `Dragon` class that uses both and adds a `roar()` method |
| `main_*.py`               | Test files for each task demonstrating usage and expected output |

---

## 🚀 How to Run

Ensure all files are executable:
```bash
chmod +x main_*.py

