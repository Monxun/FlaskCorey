FROM python:3.6.15-slim-bullseye

RUN apt-get update -y && \
    apt-get upgrade && \
    apt install git -y && \
    curl https://sh.rustup.rs -sSf | sh

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]