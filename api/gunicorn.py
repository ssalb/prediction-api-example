from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count()


bind = "0.0.0.0:{}".format(environ.get("API_PORT", 5000))
max_requests = 1024
workers = max_workers()

# accesslog = "./logs/gunicorn-access.log"
# errorlog = "./logs/gunicorn-error.log"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%({X-Real-IP}i)s"'
