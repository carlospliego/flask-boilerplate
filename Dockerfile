
FROM python:3.6.4
ENV FLASK_APP=src/server.py


# expose environments
# COPY my-env-vars /
# RUN export $(cat my-env-vars | xargs) 

COPY . /opt/app
WORKDIR /opt/app

RUN rm -rf .virtual
RUN rm -f .env
RUN python3 -m venv .virtual
RUN . .virtual/bin/activate && pip3 install -r requirements.txt && deactivate
RUN cp configs/dev .env
EXPOSE 3001

ENTRYPOINT [".virtual/bin/flask"]
CMD ["run"]