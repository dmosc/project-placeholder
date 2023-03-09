#!/bin/bash

cd ~/repos/project-placeholder;
git stash && git switch main && git fetch --all && git reset --hard origin/main;
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up --build --detach