from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@rabbit//', backend='rpc://guest@rabbitmq', )
