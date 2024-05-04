####Dockerfile to containerize application#####

FROM python:3.9-slim

WORKDIR /application

COPY requirements.txt .

RUN pip install --no-ache-dir -r requirements.txt

COPY models /models

COPY app /application/app

EXPOSE 5000

CMD ["python", "app/app.py"]
