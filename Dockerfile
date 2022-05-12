FROM python:3.9.6

LABEL maintainer="<lounah@yandex.ru>"

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
CMD ["python", "app.py"]
