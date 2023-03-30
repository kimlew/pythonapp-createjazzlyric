## Create a Jazz Lyric - Python Web App using Flask

The web app lets you:
- create a jazz lyric
- see the jazz lyric & reports the number of vowels in the lyric
- see a jazz song comprised of all the previously-created jazz lyrics
- has & uses Flask function decorators
- uses the Jinja2 text template engine
- uses a MySQL database

See a deployed version at:

`http://kimlew.pythonanywhere.com/`

See the Pipfile for the requirements and dependencies. See the Pipfile.lock for the specific versions. This app has been tested with:
- Python 3.10
- Flask 2.2.3
- Jinja2 3.1.2
- python-dotenv 1.0.0
- mysql-connector-python 8.0.32
- mysql 8.0

### To run the web app locally

#### A. Make sure you have MySQL set up locally with a new user and password.
The MySQL installation and setup differs on a Mac, on Linux, etc. Refer to sites like:

`https://database.guide/install-mysql-on-a-mac/`

`https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-22-04`


#### B. Clone the project files from GitHub.com and change to the project directory

1. Clone the repository from GitHub.com:

  `git clone https://github.com/kimlew/pythonapp-createjazzlyric`

2. Change to the project directory with:

  `cd pythonapp-createjazzlyric`


#### C. Create the MySQL database and table

1. Make sure you have the MySQL root password handy.
   
2. Run the script, `create_mysql_db.sql`, to create the database and table for the app with this command (which redirects it to the mysql command) and enter the password for the MySQL root user:
```
mysql -u root -p < ./create_mysql_db.sql
```

3. Log in to MySQL with this command and enter the password for the MySQL root user again with:
```
mysql -u root -p
```

4. Verify the database, `lyric_db` and table, `lyric` exists with:
  ```
  SHOW DATABASES;
  USE lyric_db;
  SHOW TABLES;
  DESCRIBE lyric;
  SELECT * FROM lyric;
  ```
  Note: The table is empty if it is being created for the the first time.

5. Type `exit;` to exit MySQL.

   
#### D. Create a virtual environment, install packages and dependencies, and run the app

1. Make sure you are still in the project directory, `pythonapp-createjazzlyric`.

2. Create an environment with Python 3.10 and start/activate the environment:
  ```
  python3.10 -m venv .venv
  source .venv/bin/activate         
  ```

3. Make sure you have a recent version of `pip3`. Then install the project package requirements and dependencies with:

  `pip3 install -r requirements.txt`

4. Verify the correct versions Python & Flask are installed with:

  `flask --version`

  You should see something like:

  ```
  (.venv) mac$ flask --version
  Python 3.10.10
  Flask 2.2.3
  Werkzeug 2.2.3
  ```

5. Define 4 environment variables with an appropriate host and MySQL database values, e.g., run each of these commands:

  ```
  export DB_HOST=localhost
  export DB_NAME=lyric_db
  export DB_USER=mysqlusernameonhost
  export DB_PASSWORD=mysqlpassword
  ```

  Note: The `conn_dict` variable in `conn_vars_dict.py` assigns the values to corresponding `os` module variables that the script uses.

6. Verify they are in the list of environment variables with:

  `export -p`


7.  Start the web app with:
 
  `python3 create_jazz_lyric.py`

8. See the app in the browser at:
  
  `http://localhost:5000/`

  Note: The app might not work in Chrome or Opera. If it doesn't, use **Firefox**.
