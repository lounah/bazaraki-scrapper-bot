FROM python:3.9.6

LABEL maintainer="<lounah@yandex.ru>"

ENV TZ "Europe/Moscow"
ENV LANG en_US.UTF-8

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
CMD ["python", "app.py"]
