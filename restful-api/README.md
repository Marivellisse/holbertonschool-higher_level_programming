# RESTful API Project with Flask and Python

## Overview

This project covers the fundamental concepts of developing and consuming RESTful APIs using Python.  
It introduces HTTP basics, command-line interactions, API development with built-in modules and Flask,  
and concludes with API security and authentication using industry-standard techniques.

---

## Project Structure and Tasks

### Task 0: Basics of HTTP/HTTPS
Introduces the differences between HTTP and HTTPS, the basic structure of HTTP requests/responses,  
and common HTTP methods and status codes.

### Task 1: Consume API using Command Line (curl)
Used `curl` to send GET and POST requests to the JSONPlaceholder API, inspect response headers,  
and understand HTTP communication directly from the command line.

### Task 2: Consume API using Python
Used the `requests` library to fetch data, process JSON responses, and export API output to a CSV file.

### Task 3: Develop API with http.server
Implemented a basic HTTP server using Python’s built-in `http.server` module.  
Handled routes like `/`, `/data`, and `/status` with custom JSON and text responses.

### Task 4: Develop API with Flask
Created a lightweight REST API using Flask. Implemented:
- Root and status endpoints
- Dynamic user lookup by username
- A POST endpoint to add users in memory
- Proper JSON responses and status codes

### Task 5: API Security and Authentication
Implemented:
- Basic HTTP Authentication with `Flask-HTTPAuth`
- JWT-based Authentication with `Flask-JWT-Extended`
- Custom error handlers for all token-related issues
- Role-based access control for admin-restricted routes

---

## Technologies Used

- Python 3  
- Flask  
- http.server  
- requests  
- Flask-HTTPAuth  
- Flask-JWT-Extended  
- curl

---

## How to Run

### Flask-based tasks (Task 4 and Task 5):
```bash
flask --app task_04_flask.py run
flask --app task_05_basic_security.py run

