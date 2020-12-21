FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
WORKDIR /app
COPY . /app
RUN ["pip", "install", "pipenv"]
RUN ["pipenv", "install"]
RUN ["pip", "install", "sqlalchemy"]
RUN ["pip", "install", "fastapi"]
RUN ["pip", "install", "uvicorn"]
RUN ["pip", "install", "sqlalchemy"]
RUN ["pip", "install", "psycopg2"]
RUN ["pip", "install", "alembic"]
RUN ["pip", "install", "requests"]
EXPOSE 80
CMD ["python", "main.py"]
