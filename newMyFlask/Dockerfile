

FROM python:3.6.8

WORKDIR /app

copy . .

EXPOSE 5000

RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "app.py"]


