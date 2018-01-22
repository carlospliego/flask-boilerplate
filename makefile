PYTHON = .env/bin/python3
PIP = pip3
ENV = . .env/bin/activate

install:
	virtualenv .env
	$(ENV) && $(PIP) install -r requirements.txt && deactivate # install dependencies
	# docker-compose run vendors


package:
	# `. .env/bin/activate`
	# `pip install <package>`
	# `pip freeze > requirements.txt`
	# `docker-compose run --rm vendors`
	# `deactivate`
	
	# access parameters
	
	$(ENV) && $(PIP) install $(PACKAGE)
	$(ENV) && $(PIP) freeze > requirements.txt



vendor:
	docker-compose run --rm vendors

run:
	docker-compose up -d server

	

sclean:	
	docker rm -v $(docker ps -a -q -f "status=exited") # Remove exited Docker containers
	docker rmi $(docker images -f "dangling=true" -q) # Remove all dangling images
	docker volume rm $(docker volume ls -qf "dangling=true") # Remove all dangling volumes



