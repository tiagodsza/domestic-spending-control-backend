docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=user postgres
pipenv run alembic revision --autogenerate