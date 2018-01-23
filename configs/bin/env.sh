#!/bin/bash

# the base python image
export BASE_IMG=python:3.6.4

# the directory to mount a volume with docker-compose
export MNT_WORKING_DIR=/mnt

# the directory to copy src when building an image
export DEV_WORKING_DIR=/opt/app

# ports that run locally with docker-compose
export LOCAL_PORTS='3000:5000'

# non local port
export NON_LOCAL_PORT=3001

# runtime environment file
export ENV_FILE=.env

# pip
export PIP=pip3

# virtual environment folder
export VENV_FOLDER=.virtual

# pip requirements
export PIP_REQS=requirements.txt

# application entry point
export ENTRYPOINT=src/server.py

# env configs
export ENV_CONFIGS=configs/env