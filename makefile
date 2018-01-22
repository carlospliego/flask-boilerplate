
PIP= pip3
ENV_FOLDER=.env
ENV= . $(ENV_FOLDER)/bin/activate
VENV= virtualenv $(ENV_FOLDER)
REQ= requirements.txt

install:
	$(VENV)
	$(ENV) && $(PIP) install -r $(REQ) && deactivate # install dependencies

package:
	$(ENV) && $(PIP) install $(P)
	$(ENV) && $(PIP) freeze > $(REQ)
