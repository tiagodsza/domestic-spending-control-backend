docker stop domestic-spending-control-backend

docker rm domestic-spending-control-backend

docker rmi domestic-spending-control-backend

docker build -t domestic-spending-control-backend .

docker create -p 5000:3000 --name domestic-spending-control-backend  domestic-spending-control-backend

docker start domestic-spending-control-backend

docker ps
