# Dockerfile to containerize application

FROM python:3.9-slim

WORKDIR /application

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY .  /application/

EXPOSE 5000

CMD ["python", "app.py"]
