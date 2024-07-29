FROM python:3.9

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# COPY ./postms ./accounts ./jobposts ./authors  /app/
COPY ./postms  /app/

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
