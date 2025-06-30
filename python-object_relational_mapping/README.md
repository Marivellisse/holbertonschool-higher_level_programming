# Python - Object-relational mapping

This project explores how to interact with MySQL databases using both low-level drivers like `MySQLdb` and high-level Object-Relational Mapping (ORM) tools like `SQLAlchemy`.

---

## 📚 Learning Objectives

- Understand what Object-Relational Mapping (ORM) is.
- Connect to a MySQL server from a Python script.
- Run MySQL queries from Python using `MySQLdb`.
- Prevent SQL injection in queries.
- Use SQLAlchemy to map Python classes to MySQL tables.
- Perform CRUD operations using SQLAlchemy.

---

## 🛠 Technologies Used

- Python 3.8+
- MySQL 8.0
- MySQLdb (mysqlclient)
- SQLAlchemy (ORM)
- Ubuntu 20.04 / macOS

---

## ⚙️ Setup Instructions

1. Install MySQL and Python dependencies:
   ```bash
   pip3 install mysqlclient SQLAlchemy
   ```

2. Start MySQL service and create required databases and tables using provided `.sql` files.

3. Run each script using:
   ```bash
   ./script_name.py <mysql_user> <mysql_password> <database_name> [<state_name>]
   ```

---

## 📂 Project Structure

| Filename                      | Description                                          |
|------------------------------|------------------------------------------------------|
| `0-select_states.py`         | List all states from `hbtn_0e_0_usa` (MySQLdb)       |
| `1-filter_states.py`         | List all states starting with "N"                   |
| `2-my_filter_states.py`      | Filter states by user input (vulnerable)            |
| `3-my_safe_filter_states.py` | Filter states safely (prevent SQL injection)        |
| `4-cities_by_state.py`       | List all cities with their corresponding state name |
| `5-filter_cities.py`         | List all cities of a specific state (safely)        |
| `model_state.py`             | SQLAlchemy model for `State` table                  |
| `7-model_state_fetch_all.py` | List all `State` objects using SQLAlchemy           |
| `8-model_state_fetch_first.py` | Print the first `State` object                     |
| `9-model_state_filter_a.py`  | List all states containing the letter "a"           |
| `10-model_state_my_get.py`   | Get a state by name                                 |
| `11-model_state_insert.py`   | Add a new state (`Louisiana`)                       |
| `12-model_state_update_id_2.py` | Update state name (id=2)                        |
| `13-model_state_delete_a.py` | Delete all states with "a" in name                  |
| `model_city.py`              | SQLAlchemy model for `City` table                   |
| `14-model_city_fetch_by_state.py` | List all cities with states                  |

---

## 📌 Notes

- All scripts use `MySQLdb` or `SQLAlchemy` and follow Holberton's Python style.
- Input validation is not required per project instructions.
- Scripts are executable and should not run when imported.

---

## 🧑‍💻 Author

Marivellisse Garcia  
Holberton School - Cohort 26 
