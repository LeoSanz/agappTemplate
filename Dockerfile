# To init a base image (Alpine as a very small Linux distro)
FROM python:3.12.0a6-alpine

# To update pip to minimize dependency errors
RUN pip install --upgrade pip

# To define the present working directory
WORKDIR /agapp

# To copy the contents into the working dir
ADD . /agapp

# To run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt

# To define the command to start the container
CMD ["python","app.py"]
