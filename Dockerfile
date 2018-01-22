FROM python:3.6.4
ENV FLASK_APP=src/server.py


# instad of this
COPY . /opt/app
WORKDIR /opt/app

# you should 

RUN python3 -m venv .env
RUN . .env/bin/activate && pip3 install -r requirements.txt && deactivate
EXPOSE 3000

ENTRYPOINT [".env/bin/flask"]
CMD ["run"]