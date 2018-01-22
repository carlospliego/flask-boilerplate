
PIP= pip3
VENV_DIR=.virtual
ENV_FILE= .env
CREATE_VIRTUAL_ENV= virtualenv $(VENV_DIR)
ACTIVATE_ENV= . $(VENV_DIR)/bin/activate
REQ= requirements.txt
ENV_CONFIGS=configs

install:
	rm -rf $(VENV_DIR)/ # remove .virtual directory
	rm -f $(ENV_FILE) # remove .env file
	$(CREATE_VIRTUAL_ENV)
	$(ACTIVATE_ENV) && $(PIP) install -r $(REQ) && deactivate # install dependencies
	cp $(ENV_CONFIGS)/local $(ENV_FILE)

package:
	$(ACTIVATE_ENV) && $(PIP) install $(P)
	$(ACTIVATE_ENV) && $(PIP) freeze > $(REQ)
