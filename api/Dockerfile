FROM python:3.7-slim-stretch

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-c", "gunicorn.py", "api:app"]
