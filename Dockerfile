#Deriving the latest base image
FROM python:latest

WORKDIR /usr/app/src

COPY . ./

CMD [ "python", "./main.py"]