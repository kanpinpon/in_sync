FROM --platform=linux/amd64 python:3.8.12-slim

COPY api /api
COPY requirements_docker.txt /requirements.txt

RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx ffmpeg && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
