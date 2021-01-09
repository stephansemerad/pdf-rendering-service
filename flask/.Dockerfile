FROM python:3.7.2-strech

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ["uswgi", "app.ini"]

