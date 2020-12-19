import os

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'controle_gastos')
DB_PORT = os.getenv('DB_PORT', '5432')
API_PORT = os.getenv('API_PORT', '3000')
API_HOST=os.getenv('API_HOST', 'localhost')
URL_DB = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
