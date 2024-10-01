from typing import Optional

from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@rabbit//', backend='rpc://guest@rabbitmq')


class Dispatcher:
    """
    Interface for handing execution
    """
    pass


class Fetcher:
    """
    Interface for receiving info back
    """
    pass


@app.task(name='execute_static')
def execute_static(mod: str, cls: Optional[str] = None, func: Optional[str] = None, *args, **kwargs):
    import importlib
    modl = importlib.import_module(mod)
    return dir(modl)

# @app.task(name='create_request')
# def create_request(request: Request):
