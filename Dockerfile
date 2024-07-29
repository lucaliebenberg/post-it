FROM python:3.9

RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY .  /app

WORKDIR /app

COPY ./entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
