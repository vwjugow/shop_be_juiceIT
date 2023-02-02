# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
RUN rm -rf /var/app
RUN mkdir /var/app
WORKDIR /var/app
COPY requirements requirements
RUN pip3 install -r requirements/docker.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
