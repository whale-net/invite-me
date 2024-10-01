from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@rabbit//', backend='rpc://guest@rabbitmq')


@app.task(name='add')
def add(x, y):
    print("in add")
    return x+y
