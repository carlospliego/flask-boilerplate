FROM mongo

COPY users.json /users.json
CMD mongoimport --host mongodb --db flask --collection user --type json --file /users.json --jsonArray