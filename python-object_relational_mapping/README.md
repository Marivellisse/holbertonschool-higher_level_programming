# Python - Object-relational mapping

## Description
This project demonstrates the interaction between Python and MySQL using both MySQLdb and SQLAlchemy. It includes various operations like selecting, filtering, and inserting data into databases, as well as creating models using ORM.

## Requirements
- Python 3.8
- MySQL 8.0
- `mysqlclient` (MySQLdb) v2.0.x
- SQLAlchemy v1.4.x
- Ubuntu 20.04

## File List

| Filename               | Description |
|------------------------|-------------|
| 0-select_states.py     | Lists all states in the DB |
| 1-filter_states.py     | Lists all states starting with N |
| 2-my_filter_states.py  | Filters states by user input (not safe) |
| 3-my_safe_filter_states.py | Safe filtering using parameterized queries |
| 4-cities_by_state.py   | Lists all cities and their states |
| 5-filter_cities.py     | Lists all cities in a specific state |

## How to run
```bash
./0-select_states.py <username> <password> <database_name>
```
