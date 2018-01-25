# boiler_flask


A Python boilerplate for services using Flask, wrapped in venv inside a Docker
container.

*Runtime architecture*
```
Docker
    Venv ( python virtual environment )
        Flask ( micro-framework )

```

## Development

### Host Requirements
* python 3.6 ( this is just needed to create the virtual environment )
* make
* gettext `brew install gettext && brew link --force gettext`
* npm, node ( some version )


### Installation
*install node_modules*
`npm install`

*This will first create the necesary make and docker files This will also create a virtual environment, activate the environment, then installs
dependencies*

`sh ./scripts/init.sh && make reset`


### Installing a python package
*Please use this command instead of using pip. This can be run inside or outside the activated virtual environment. This script is a benefit as it freezes requirements into > requirements.txt*
`make package p=<package>`

### Running a container
*This will run the script defined in `docker-compose.yml`. It is important to 
note that this script will create a volume pointing to your local source code and
`.venv` folder*

`docker-compose up`


## Deployment
*This is a bit of a different path than running `docker-compose` as this uses
the `Dockerfile` to take advantage of the `COPY` command so that these images can 
contain all of the source necessary to self execute w/ out volumes.*

### Strategy
Get an instance of mongo from DockerHub
`docker pull mongo`

Create a mongo container called mongodb
`docker run --name mongodb -d -v $(pwd)/data/db:/data/db mongo`

Build or checkout your image
`docker build -t <img-tag> . -f <Dockerfile>`

Run a container, linking it to mongodb
`docker run --name <container-name> -d -p <ports> --link mongodb <img-tag>`


## Common Docker

### Build Image
`docker build -t <img-tag> . -f <Dockerfile>`

### Running a container
#### Database
since the service container depends on the database, you'll want to run this first
`docker run --name mongodb -d -v $(pwd)/data/db:/data/db mongo`

#### Service
notice the linking
`docker run -d --name flask-app -p <ports> --link mongodb <img-tag>`

### Running Mongo In Shell
`docker exec -it <container-id> mongo`


## Versioning
We use SemVer for versioning.

## Author
* Carlos Pliego *@carlosjpliego*

