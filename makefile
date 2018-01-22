PYTHON = .env/bin/python3
PIP = pip3
ENV = . .env/bin/activate

oldinstall:
	python3 -m venv .env
	$(ENV) && $(PIP) install -r requirements.txt && deactivate # install dependencies
	cp example.env_ .env_




vendor:
	docker-compose run --rm vendors

run:
	docker-compose up -d server

	

sclean:	
	docker rm -v $(docker ps -a -q -f "status=exited") # Remove exited Docker containers
	docker rmi $(docker images -f "dangling=true" -q) # Remove all dangling images
	docker volume rm $(docker volume ls -qf "dangling=true") # Remove all dangling volumes



