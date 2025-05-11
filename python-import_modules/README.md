# Python - Import & Modules

This project focuses on the fundamentals of importing and using modules in Python, including how to:

- Import specific functions from a file
- Use built-in modules like `sys`
- Handle command-line arguments
- Write scripts that only execute when run directly
- Explore `.pyc` files
- Avoid wildcard imports (`from module import *`)

## 📁 Project Directory: `python-import_modules`

### 🧠 Key Concepts Covered:
- `import` vs `from ... import ...`
- `__name__ == "__main__"` usage
- `sys.argv` and command-line arguments
- Using `.pyc` compiled files
- Accessing module variables and functions safely

---

## 📌 Files & Description

| File | Description |
|------|-------------|
| `0-add.py` | Imports `add(a, b)` from `add_0.py` and prints the result of 1 + 2 |
| `1-calculation.py` | Imports math functions from `calculator_1.py` and performs add, sub, mul, div |
| `2-args.py` | Prints the number and list of arguments passed to the script |
| `3-infinite_add.py` | Adds all arguments passed via command line |
| `4-hidden_discovery.py` | Prints all names defined in a compiled module that do not start with `__` *(run in sandbox)* |
| `5-variable_load.py` | Imports and prints the value of variable `a` from `variable_load_5.py` |

---

## 🛠 Usage

To run each script:

```bash
chmod +x filename.py
./filename.py [arguments...]

