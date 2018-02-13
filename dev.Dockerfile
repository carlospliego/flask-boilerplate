FROM python:3.6.4

COPY . /mnt
WORKDIR /mnt

RUN python3 -m venv .virtual
RUN . .virtual/bin/activate && pip install -U -r requirements.txt && deactivate
RUN cp env/local .env
EXPOSE 3000

ENTRYPOINT [".virtual/bin/python"]
CMD ["src/run.py"]