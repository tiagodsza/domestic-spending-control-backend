FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip3 install pipenv
RUN pipenv install
EXPOSE 3000
CMD pipenv run python main.py
