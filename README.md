# boiler_flask


A Python boilerplate for services using Flask, wrapped in venv inside a Docker
container.

*High level architecture*
```
Docker
    Venv ( python virtual environment )
        Flask ( micro-framework )

```

## Development

### Host Requirements
* python 3.6 ( this is just needed to create the virtual environment )
* make
* gettext
```
brew install gettext
brew link --force gettext

```

### Installation
*This will first create the necesary make and docker files This will also create a virtual environment, activate the environment, then installs
dependencies*
`make -f init.make && make install-local`

### Installing a python package
*Please use this command instead of using pip. This can be run inside or outside the activated virtual environment. This script is a benefit as it freezes requirements into > requirements.txt*
`make package p=<package>`

### Running a container
*This will run the script defined in `docker-compose.yml`. It is important to 
note that this script will create a volume pointing to your local source code and
`.venv` folder*

`docker-compose up -d server`


## Deployment Notes <to be finished>
*This is a bit of a different path than running `docker-compose` as this uses
the `Dockerfile` to take advantage of the `COPY` command so that these images can 
contain all of the source necessary to self execute w/ out volumes.*

### build an image
`docker build -t <img-tag> . -f <Dockerfile>`

### start a container
`docker run -d --name <container-name> -p 3001:5000 <img-tag>`

## Versioning
We use SemVer for versioning.


## Author
* Carlos Pliego *@carlosjpliego*

