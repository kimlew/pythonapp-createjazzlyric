## Create a Jazz Lyric - Python Web App using Flask

The web app lets you:
- create a jazz lyric
- see the jazz lyric & reports the number of vowels in the lyric
- see a jazz song comprised of all the previously-created jazz lyrics

View a deployed version at: `http://kimlew.pythonanywhere.com/`

This app:
- has & uses Flask function decorators
- uses the Jinja2 text template engine

This app has been tested with:
- Python 3.10
- Flask 2.2.3
- Jinja2 3.1.2
- python-dotenv 1.0.0
- mysql-connector-python 8.0.32
- mysql 8.0  

See the Pipfile for the requirements and dependencies. See the Pipfile.lock for the specific versions.

### To run the web app locally

1. Clone the repo: `git clone https://github.com/kimlew/pythonapp-createjazzlyric`

2. Change directory: `cd pythonapp-createjazzlyric`
   
3. Install pipenv: `pip3 install pipenv`

4. Install required packages and dependencies into the virtual environment with: `pipenv install`
   
5. Start the virtual environment: `pipenv shell`

6. In the virtual environment, start the web app with: `python3 create_jazz_lyric.py`

7. In the browser, go to: `http://localhost:5000/`
