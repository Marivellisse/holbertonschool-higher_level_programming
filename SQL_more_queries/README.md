SQL - Introduction & More Queries
This project is part of the Holberton School curriculum and focuses on deepening SQL knowledge, including database design, user management, advanced constraints, and complex queries. It also covers practical data manipulation and joins, preparing students for real-world relational database use cases.
Learning Objectives
- Create MySQL users and assign privileges
- Use constraints: PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE
- Perform advanced SELECT queries including JOINs, UNIONs, and subqueries
- Import data from external sources (e.g., SQL dump files)
- Design relational models and enforce integrity rules
- Use MySQL functions: COUNT, AVG, MAX, etc.
- Manage default values and ensure data consistency
Environment
- OS: Ubuntu 20.04 LTS or macOS with MySQL via Homebrew
- MySQL: version 8.0.25+
- SQL queries executed via:
  cat file.sql | mysql -u root -p [database_name]

File Structure & Task Summary
File	Description
0-privileges.sql	List privileges for user_0d_1 and user_0d_2
1-create_user.sql	Create user_0d_1 with all privileges
2-create_read_user.sql	Create user_0d_2 with SELECT privilege only on database hbtn_0d_2
3-force_name.sql	Create table force_name with name NOT NULL
4-never_empty.sql	Create table id_not_null with default value 1
5-unique_id.sql	Create table unique_id with UNIQUE constraint on id
6-states.sql	Create database hbtn_0d_usa and table states
7-cities.sql	Create table cities with FOREIGN KEY to states.id
8-cities_of_california_subquery.sql	List cities of California using subquery
9-cities_by_state_join.sql	List cities and their states using JOIN
10-genre_id_by_show.sql	List shows with their genre_id
11-genre_id_all_shows.sql	List all shows and genre_id, NULL if no genre
12-no_genre.sql	List shows with no genre linked
13-count_shows_by_genre.sql	Count shows per genre
14-my_genres.sql	List genres of show 'Dexter'
15-comedy_only.sql	List shows that belong to genre 'Comedy'
16-shows_by_genre.sql	List all shows and genres using LEFT JOIN

All SQL files follow the required syntax:
•	- Begin with a comment describing the task
•	- Use UPPERCASE for SQL keywords
•	- End with a newline
•	- No forbidden commands like SELECT or SHOW when not allowed

