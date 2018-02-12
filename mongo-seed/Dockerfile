FROM mongo

COPY users.json /users.json
RUN mongoimport --host mongodb --db flask --collection user --type json --file /users.json --jsonArray --drop