PYTHON = .env/bin/python3
PIP = pip3
ENV = . .env/bin/activate

install:
	python3 -m venv .env
	$(ENV) && $(PIP) install -r requirements.txt && deactivate # install dependencies