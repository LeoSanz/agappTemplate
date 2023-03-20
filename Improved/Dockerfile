# Specifies the base image to use for building the Docker image.
FROM python:alpine:3.17

# Updates the package lists in the container and installs the specified packages, and removes the package lists to reduce the size of the container.
RUN apt-get update \  
    && apt-get install -y nginx supervisor haproxy \ # Installs Nginx, Supervisor, and HAProxy packages in the container.
    && rm -rf /var/lib/apt/lists/* # Removes the package lists to reduce the size of the container.

# Copies the requirements.txt file to the /app directory in the container.
COPY requirements.txt /app/requirements.txt 

# Installs the Python packages listed in the requirements.txt file.
RUN pip install --no-cache-dir -r /app/requirements.txt 

# Copies all the files in the current directory to the /app directory in the container.
COPY . /app 

# Removes the default Nginx configuration file.
# Creates a symbolic link to the custom Nginx configuration file.
RUN rm -f /etc/nginx/sites-enabled/default \ 
    && ln -s /app/nginx.conf /etc/nginx/sites-enabled/ 

# Informs Docker that the container listens on port 80 and allows incoming connections.
EXPOSE 80 

# Specifies the command that should be executed when the container starts, which is to run the supervisord process with the configuration file located at /app/supervisord.conf.
CMD ["supervisord", "-c", "/app/supervisord.conf"] 
