FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update -y && \
    apt-get install -y git

RUN pip install -r requirements.txt

COPY ./app /app