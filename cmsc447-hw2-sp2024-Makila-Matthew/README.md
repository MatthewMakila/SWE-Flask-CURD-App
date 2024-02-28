# SWE HW 2: CRUD Application using Flask
* I am creating a web application to create, read, update, and delete information from a database!

# Run Instructions
* Initiate a venv

### Setup the database:
* **Once only** Run `init_db.py` to initialize database with sample data

### Running the flask application and accessing the web server: 
* cd into the proper directory: `cd cmsc447-hw2-sp2024-Makila-Matthew`
* Initiate the command: `set FLASK_APP=app` (windows) or `export FLASK_APP=app` (mac)
* Initiate the command: `set FLASK_ENV=development` (windows) or `export FLASK_ENV=development` (mac)
* In the command line, `flask run` and follow the provided URL

### Using the webpage:
* From the home screen, you can simply press **Create User** and fill in information to create a new user
* You can also press **Search User** and then type in a partially-matching username or complete ID to search the database!
* The **Edit** button on the search page allows you to adjust the name and points, or **Delete** a user

# Dependencies and Libraries
* Must have installed virtual environment `venv`
* Then install Flask (`flask`) & database packages (`databases`, `db-sqlite3`) with `pip install [the_package_names]`
