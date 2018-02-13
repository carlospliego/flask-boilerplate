# mongodb:
#     image: mongo:latest
#     container_name: "mongodb"
#     environment:
#             - MONGO_DATA_DIR=/mongo/data/db
#             - MONGO_LOG_DIR=/dev/null
#     volumes:
#       - ./mongo/data/db:/data/db
#     ports:
#         - 27017:27017
#     command: mongod --logpath=/dev/null #--smallfiles --logpath=/dev/null # --quiet


FROM mongo:latest

# ENV TZ=America/New_York
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# COPY mongod.conf /etc/mongod.conf

CMD ["mongod"]
EXPOSE 27017
EXPOSE 28017