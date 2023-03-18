FROM python:3.9-slim-buster

RUN apt-get update \
    && apt-get install -y nginx supervisor haproxy \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

RUN rm -f /etc/nginx/sites-enabled/default \
    && ln -s /app/nginx.conf /etc/nginx/sites-enabled/

EXPOSE 80

CMD ["supervisord", "-c", "/app/supervisord.conf"]
