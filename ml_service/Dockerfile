FROM python:3.7-slim-stretch

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "model_process.py"]
