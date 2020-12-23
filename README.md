 # Introduction 
###1. Description:
    This is an "api" to record and track household expenses. This project aims to develop my skills in the technologies listed below.
###2. Technologies used:
    a. Python
    b. FastAPI    
    c. SQLAlchemy
    d. Alembic
###3. Tests
    a. 100% test coverage
    b. Used Unittest and pytest
 
# Getting Started
###1.	Requeriments
    a. Python 3.8+

###2. Install
    a. Configure the settings in the "config" file at the root:
       Create a .env with variables of the config or configure the envirnment variables.
    b. pip3 install pipenv
    c. pipenv install
    d. Create Database: pipenv run alembic upgrade head
    
###3. Run Tests
    a. pytest --cov=app 
    b. pytest --cov=app/ --cov-report=html
    
###4. Run Application
    a.python main.py
    