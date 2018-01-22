
# Local Dev
## Install
`make install`

## Installing a python package process
`make package PACKAGE=Django`

## Start a container
`docker-compose up -d server`


# dev/stg/prod

## build an image
`docker build -t <img-tag> .`

## start a container
`docker run -d --name <container-name> -p 3000:5000 <img-tag>`








#Requirements
Python 3.6^


## Install Requirements
`make install`

## Activate Environment
`. .env/bin/activate`

## Install package and save requirements ( do this inside the environment )
`pip3 install package`
`pip3 freeze > requirements.txt`




Install dependencies
## vendor:
	docker-compose run --rm vendors

## run
	docker-compose up -d server