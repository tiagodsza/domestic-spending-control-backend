 # Introduction 
1. Description:
    <p>This is an "api" to record and track household expenses. This project aims to develop my skills in the technologies listed below.<p>
2. Tecnologias utilizadas:
    <p>a. Python</p>
    <p>b. FastAPI</p>    
    <p>c. SQLAlchemy</p>
    <p>d. Alembic</p>
3. Testes
    <p>a. 100% de cobertura</p>
    <p>b. Utilizado Unittest e pytest</p>
 
# Getting Started
1.	Requeriments
    a. Python 3.8+

2. Install
    <p>a. Configure the settings in the "config" file at the root.</p>
    <p>b. pip3 install pipenv</p>
    <p>c. pipenv install</p>
    <p>d. Create Database: pipenv run alembic upgrade head</p>
    
3. Run Tests    
    <p>a. pytest --cov=app</p> 
    <p>b. pytest --cov=app/ --cov-report=html</p>
    
4. Run Application
    <p>a.python main.py</p>  
    