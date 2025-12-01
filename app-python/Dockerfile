# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install flask --no-cache-dir

COPY . .

EXPOSE 8000

CMD ["python", "./app.py"]

