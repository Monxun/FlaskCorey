FROM python:3.6.15-slim-bullseye

RUN apt-get update -y && \
    apt-get upgrade && \
    apt install git -y && \
    apt install curl -y && \
    curl https://sh.rustup.rs -sSf | sh -y && \
    git clone https://github.com/rust-lang/cargo && \
    mkdir cargo && \
    cd cargo && \
    cargo build --release && \
    cd /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]