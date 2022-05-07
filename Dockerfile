FROM python:latest

WORKDIR /usr/app/src

COPY . ./

EXPOSE 8443

RUN pip install -r requirements.txt

CMD [ "python", "./main.py"]