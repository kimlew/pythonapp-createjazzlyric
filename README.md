## Create a Jazz Lyric - Python Web App using Flask

The web app lets you:
- create a jazz lyric
- see the jazz lyric & reports the number of vowels in the lyric
- see a jazz song comprised of all the previously-created jazz lyrics
- has & uses Flask function decorators
- uses the Jinja2 text template engine

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


#### B. Create a Python environment and get the project files

1. Clone the repo:
  
  **For PR**:

  `git clone -b python3-10_pipenv https://github.com/kimlew/pythonapp-createjazzlyric`

  **After PR merged**:

  `git clone https://github.com/kimlew/pythonapp-createjazzlyric`

1. Change to the project directory with:
 
  `cd pythonapp-createjazzlyric`

3. Create a Python environment with version 3.10:
 
  `python3.10 -m venv .venv`


#### C. Create MySQL database and table

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
Note: The table should be empty if it is being created for the the first time.

5. Type `exit;` to exit MySQL.
   
#### C. Get dependencies and run the app
1. Make sure you are still in the project directory `pythonapp-createjazzlyric`.

2. Install pipenv:
 
  `pip3 install pipenv`

3. Install required packages and dependencies into the virtual environment with:
   
  `pipenv install`
   
4. Start the virtual environment:
  
  `pipenv shell`

5. In the virtual environment, start the web app with:
 
  `python3 create_jazz_lyric.py`

6. In the browser, go to:
  
  `http://localhost:5000/`
