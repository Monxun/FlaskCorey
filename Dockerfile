FROM python:3.6

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get install -y gunicorn

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./project /code/app

CMD ["gunicorn", "--conf", "app/gunicorn_conf.py", "--bind", "0.0.0.0:5000", "app.run:app"]