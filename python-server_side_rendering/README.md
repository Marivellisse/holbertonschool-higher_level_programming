# Python - Server-Side Rendering

## Description

This project focuses on implementing server-side rendering (SSR) using Python and the Flask framework. Server-side rendering generates fully formed HTML content on the server and delivers it to the client, improving SEO, performance, and user experience compared to client-side rendering. The project also integrates the Jinja2 templating engine to dynamically generate web pages and read data from various sources including JSON, CSV, and SQLite.

---

## Learning Objectives

By the end of this project, you should be able to:

- Understand the difference between server-side and client-side rendering
- Implement SSR in Python using Flask
- Use the Jinja2 templating engine to render dynamic HTML content
- Reuse HTML components using Jinja’s `{% include %}` directive
- Read and process data from JSON, CSV, and SQLite sources
- Use Jinja control structures such as loops and conditionals
- Handle dynamic routes and query parameters in Flask
- Implement error handling for invalid inputs or missing data

---

## Project Structure

python-server_side_rendering/
├── templates/
│ ├── index.html
│ ├── about.html
│ ├── contact.html
│ ├── items.html
│ ├── product_display.html
│ ├── header.html
│ └── footer.html
├── static/ (optional)
│ └── style.css
├── products.json
├── products.csv
├── products.db
├── items.json
├── template.txt
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── task_03_files.py
├── task_04_db.py
└── README.md

Tasks Overview
Task 0: Generate Invitations from Template
Function: generate_invitations(template, attendees)
Input: Template string and list of dictionaries
Output: Creates output files named output_1.txt, output_2.txt, etc.
Handles missing data with "N/A" and validates input types
Task 1: Basic Flask App with Reusable Templates
Route: /, /about, /contact
Templates include reusable header.html and footer.html
Renders static content using Jinja2
Task 2: Dynamic Page with Jinja Loops and Conditionals
Route: /items
Loads data from items.json
Displays list of items or fallback message if empty
Task 3: Display Products from JSON or CSV
Route: /products?source=json or source=csv with optional id query
Displays data in table format using Jinja2
Handles errors for invalid sources and missing products
Task 4: Integrate SQLite Data Source
Extends /products?source=sql to read from products.db
Uses SQLite SELECT queries to retrieve product data
Same output template as Task 3 with unified logic
Example URLs to Test
http://localhost:5000/
http://localhost:5000/about
http://localhost:5000/contact
http://localhost:5000/items
http://localhost:5000/products?source=json
http://localhost:5000/products?source=csv&id=2
http://localhost:5000/products?source=sql&id=1
Resources
Flask Documentation
Jinja2 Documentation
Python JSON Docs
Python CSV Docs
Python SQLite Docs
MDN Server-Side Development

Author: Marivellisse Garcia
