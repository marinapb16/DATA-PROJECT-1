FROM python:3.9.15-slim-buster


RUN mkdir /app
WORKDIR /app


COPY . /app

RUN pip install psycopg2
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "main.py"]