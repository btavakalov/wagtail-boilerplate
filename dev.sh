#!/bin/bash

cp .env.dev .env

DOCKER_COMPOSE='docker-compose -f docker-compose.yml -f docker-compose.dev.yml -p wagtail'

case $1 in
  up)
    ${DOCKER_COMPOSE} up --build -d
    ./dev.sh logs
  ;;
  build)
    ${DOCKER_COMPOSE} build
  ;;
  down)
    ${DOCKER_COMPOSE} down
  ;;
  start)
    ${DOCKER_COMPOSE} start $2
  ;;
  stop)
    ${DOCKER_COMPOSE} stop $2
  ;;
  restart)
    ${DOCKER_COMPOSE} restart $2
    ./dev.sh logs $2
  ;;
  logs)
    ${DOCKER_COMPOSE} logs -f --tail=100 $2
  ;;
  bash)
    ${DOCKER_COMPOSE} exec --user=root $2 bash
  ;;
  exec)
    ${DOCKER_COMPOSE} exec $2 $3
  ;;
esac