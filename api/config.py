import os

API_VERSION = 1

DB_HOST = os.environ["REDIS_HOST"]
DB_PORT = int(os.environ["REDIS_PORT"])
DB_NAME = int(os.environ["REDIS_ID"])

DB_QUEUE = os.environ["INPUT_QUEUE"]
CLIENT_SLEEP = 0.25
