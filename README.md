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
* npm install -g newman

### Integration Server
* same as host

### Installation
* `npm install`
* `gulp install`

### Changing ENV settings
* `gulp env`

### IDE Setup
Make sure that your python interpreter is reading from the .virtual directory 

### Running

Running the application and database container. Modifying files will not refresh the container as the volumes 
for these containers are on the host system
`docker-compose up`

### Unit Testing

* `gulp unit`
* `gulp unit-w`

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


# Development Notes

For seed information : have the following extera docker containers:

* dev-seed
    This will be responsible for establishing a connection with the datbase container. By executing after the mounting of that container. 
    The algorithm would look something like this:

    // establish connection

    NAMES = {
        names = [
            'Bill',
            'Dave',
            'Andy',
            'Roger',
            'Homer',
            'Peter'
        ]
        random()=>{
            return (names[Math.random() * (names.length)]) ? 'Default'
        }
    }
    const schema = [
        {run: 'create', create:'db'},
        {create:'col'}, // or {create:'collection'}
        {
            insert:{
                name: ()=>{
                    return NAMES.random()
                }
            }
            
        }
    ]

    <!-- const data = [{
        apply:(s)=>{
            return connectionHandler.execute(this); 
        }      
    }]// iteratable objects  -->

    actions = {
        create:(args)=>{
            // .. create
            'col'
        }
        insert:(args)=>{
            // .. insert
        }
    }

    for i in schema:
        i.run // what to do
        i[i.run]//what to run
        actions[i.run](i[i.run])
    
* migrate