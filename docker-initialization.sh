docker stop domestic-spending-control
docker stop dsc-db
docker rm domestic-spending-control
docker rm dsc-db
docker rmi domestic-spending-control-backend_api-backend
docker rmi postgres
docker-compose up -d
pipenv run alembic upgrade head