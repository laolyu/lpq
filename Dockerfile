# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python3","run_cmd.py"]