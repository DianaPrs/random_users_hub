FROM python:3.8

ENV FLASK_APP "webapp/__init__.py"
ENV FLASK_ENV "development"

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD flask run --host=0.0.0.0