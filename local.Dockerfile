#production one first

FROM python:3.6.4
ENV FLASK_APP=app/app.py


# instad of this
COPY . /app
WORKDIR /app

# you should 

RUN python3 -m venv .env
RUN . .env/bin/activate && pip3 install -r requirements.txt && deactivate
EXPOSE 3000

ENTRYPOINT [".env/bin/flask"]
CMD ["run"]
