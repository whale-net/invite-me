from celery import Celery


def _execute_obj(obj, func, *args, **kwargs):
    return getattr(obj, func)(*args, **kwargs)


app = Celery('tasks', broker='pyamqp://guest@rabbit//', backend='rpc://guest@rabbitmq', )
