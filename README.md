# boiler_flask


A Python boilerplate for services using Flask, wrapped in venv inside a Docker
container.

*Runtime architecture*
```
Application Service Container
    Venv ( python virtual environment )
        Flask ( micro-framework )
        
Database Docker Container
    ENV ( data reference to parent file system ) 
    DBMS & tooling processes

```

## Development

### Host Requirements
* python 3.6^
* virtualenv
* node
* npm install -g gulp
* Docker CE

### Installation
* `npm install`
* `gulp install`


### IDE Setup
Make sure that your python interpreter is reading from the .virtual directory 

### Running

Running the application and database container. Modifying files will not refresh the container as the volumes 
for these containers are on the host system
`docker-compose up`


## Deployment
*This is a bit of a different path than running `docker-compose` as this uses
the `Dockerfile` to take advantage of the `COPY` command so that these images can 
contain all of the source necessary to self execute w/ out volumes.*

### Strategy
Get an instance of mongo from DockerHub
`docker pull mongo`

Create a MongoDB container called mongodb
`docker run --name mongodb -d -v $(pwd)/data/db:/data/db mongo`

Build or checkout your image
`docker build -t <img-tag> . -f <Dockerfile>`

Run a container, linking it to mongodb
`docker run --name <container-name> -d -p <ports> --link mongodb <img-tag>`


## Common Docker

### Build Image
`docker build -t <img-tag> . -f <Dockerfile>`

### Running a containers manually
#### Database
since the service container depends on the database, you'll want to run this first
`docker run --name mongodb -d -v $(pwd)/data/db:/data/db mongo`

#### Service
notice the linking
`docker run -d --name flask-app -p <ports> --link mongodb <img-tag>`

### Running Mongo In Shell
`docker exec -it <container-id> mongo`

### Running containers via docker-compose ( development only )
`docker-compose up`

## Versifying
We use SemVer for versifying.

