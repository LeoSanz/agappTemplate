FROM python:alpine:latest 
RUN apk add --no-cache build-base python3-dev libffi-dev openssl-dev nginx 
WORKDIR /opt/api 
COPY api/requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt 
COPY api/ /opt/api/ 
COPY docker-entrypoint.sh /bin/docker-entrypoint 
COPY haproxy.cfg /etc/haproxy/haproxy.cfg 
CMD ["/bin/docker-entrypoint"] 
