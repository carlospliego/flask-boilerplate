FROM python:3.6.4

COPY . /opt/app
WORKDIR /opt/app

RUN rm -rf .virtual
RUN rm -f .env
RUN python3 -m venv .virtual
RUN . .virtual/bin/activate && pip3 install -U -r requirements.txt && deactivate
RUN cp env/dev .env
EXPOSE 3001

ENTRYPOINT [".virtual/bin/python"]
CMD ["src/run.py"]