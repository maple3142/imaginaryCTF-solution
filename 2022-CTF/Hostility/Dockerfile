FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app

RUN pip3 install flask Flask-Limiter requests

COPY server.py /app
COPY flag.txt /app
COPY upload.html /app
COPY Dockerfile /app

RUN mkdir /app/uploads
RUN chmod -R 555 /app
RUN chmod -R 777 /app/uploads

ENTRYPOINT [ "python3" ]

CMD [ "server.py" ]