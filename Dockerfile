FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip3 install fastapi
RUN pip3 install uvicorn
RUN pip3 install sqlalchemy
RUN pip3 install sqlalchemy
RUN pip3 install psycopg2
RUN pip3 install alembic
RUN pip3 install requests
CMD python main.py
