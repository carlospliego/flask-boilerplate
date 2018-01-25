#!/usr/bin/env bash


# Setup virtualenv located in .virtual and install dependencies

# include settings
. ./dev_scripts/settings.sh

# create virtual environment
virtualenv ${VENV_FOLDER}

# start the virtual environment and install dependencies
. ${VENV_FOLDER}/bin/activate && ${PIP} install -r ${PIP_REQS} && deactivate