#Deriving the latest base image
FROM python:latest

WORKDIR /usr/app/src

COPY . ./

CMD [ "pip3", "install", "-r", "requiremets.txt" ]
CMD [ "python", "./main.py"]