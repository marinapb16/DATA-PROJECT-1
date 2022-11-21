FROM python:3.9


RUN mkdir /app
WORKDIR /app


COPY . /app


RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python", "main.py"]
