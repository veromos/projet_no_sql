#!/bin/sh
docker kill $(docker ps -q)
docker-compose up -d
docker exec ESGI_MONGO /home/mongo/import_db.sh
