#!/bin/bash
mkdir -p data
sudo docker stop postgres
sudo docker rm postgres
sudo docker build -t gtoken/gtoken-postgres-box .
sudo docker run -d -p 5432 --name postgres -e DB_USER=gtokendb -e PGDATA=/srv/data -v $PWD/data:/srv/data gtoken/gtoken-postgres-box
