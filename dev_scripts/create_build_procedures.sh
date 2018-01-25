#!/usr/bin/env bash

#this file will just create the development and docker files from the file_template


source dev_scripts/settings.sh; rm -rf docker-compose.yml; envsubst < "dev_scripts/file_templates/docker/docker-compose.yml" > "docker-compose.yml";
source dev_scripts/settings.sh; rm -rf dev.Dockerfile; envsubst < "dev_scripts/file_templates/docker/dev.Dockerfile" > "dev.Dockerfile";
source dev_scripts/settings.sh; rm -rf prod.Dockerfile; envsubst < "dev_scripts/file_templates/docker/prod.Dockerfile" > "prod.Dockerfile";
source dev_scripts/settings.sh; rm -rf .dockerignore; envsubst < "dev_scripts/file_templates/docker/.dockerignore" > ".dockerignore";
