cat << EOF > README.md
# Python - Input/Output

## 📚 Description

This project covers the basics of input/output in Python. It includes reading and writing files, understanding the `with` statement, working with file cursors, and using JSON for serialization and deserialization. The project also demonstrates how to use command-line arguments with the `sys` module.

## 🧠 Learning Objectives

- How to open, read, and write files in Python
- Use the `with` statement for proper file handling
- Understand file cursor movement
- Ensure proper file closure
- What is JSON and how to use it
- Serialization and deserialization of data
- How to handle command-line arguments in Python

## 🛠️ Requirements

- Python 3.8.5
- `pycodestyle` 2.7.*
- All scripts are executable and include a proper shebang (`#!/usr/bin/python3`)
- All test files are in the `tests` folder and executed with `python3 -m doctest ./tests/*`

## 📂 Project Structure

- `0-read_file.py`: Reads and prints a text file
- `1-write_file.py`: Writes text to a file
- Additional tasks involve appending text, JSON handling, and file evaluation

## 📁 Folder

- `tests/`: Contains `.txt` files for doctest-based testing.

## 📌 Usage

```bash
./0-main.py

