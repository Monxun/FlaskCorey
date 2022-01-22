FROM python:3.6

RUN apt-get update -y && \
    apt-get install -y git

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD export FLASK_APP=run.py && \
    export FLASK_ENV=development && \
    python app/run.py