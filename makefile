
PIP= pip3
VENV_DIR=.virtual
ENV_FILE= .env
CREATE_VIRTUAL_ENV= virtualenv $(VENV_DIR)
ACTIVATE_ENV= . $(VENV_DIR)/bin/activate
REQ= requirements.txt
ENV_CONFIGS=configs

install:
	source configs/docker/env.sh; rm -rf docker-compose.yml; envsubst < "configs/docker/docker-compose.yml" > "docker-compose.yml";
	source configs/docker/env.sh; rm -rf Dockerfile; envsubst < "configs/docker/Dockerfile" > "Dockerfile";
	rm -rf $(VENV_DIR)/
	rm -f $(ENV_FILE)
	$(CREATE_VIRTUAL_ENV)
	$(ACTIVATE_ENV) && $(PIP) install -r $(REQ) && deactivate
	cp $(ENV_CONFIGS)/local $(ENV_FILE)

package:
	$(ACTIVATE_ENV) && $(PIP) install $(P)
	$(ACTIVATE_ENV) && $(PIP) freeze > $(REQ)
