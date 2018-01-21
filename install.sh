# This script creates and starts a new environment then installs dependencies
virtualenv .env && source .env/bin/activate && pip install -r requirements.txt && deactivate``
