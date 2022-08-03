echo killing old docker processes
docker-compose rm -fs

echo building docker containers
docker-compose up --build -d
#docker build -t flask_project:0.2.1
#docker stack deploy -c docker-compose.yml secret