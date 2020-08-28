# controle-de-gastos-backend
Application to control domestic spending.
Container que inicia o banco de dados.
    docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=user postgres
Comando para gerar as versões do banco
    pipenv run alembic revision --autogenerate
    
Configurar variáveis de ambiente com:
    HOST
    DATABASE_USER
    DATABASE_PASSWORD
    PORT