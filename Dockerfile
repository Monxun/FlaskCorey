FROM python:3.6

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./project /code/app

CMD ["gunicorn", "--conf", "app/gunicorn_conf.py", "--bind", "0.0.0.0:80", "app.run:app"]