FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN /run.sh

COPY ./project /app