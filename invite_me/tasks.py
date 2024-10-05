import pickle
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


@app.task(name="execute_obj")
def execute_obj(obj, func, *args, **kwargs):
    return pickle.dumps(getattr(pickle.loads(obj), func)(*args, **kwargs))


@app.task(name='execute_static')
def execute_static(module: str, cls: Optional[str] = None, func: Optional[str] = None, *args, **kwargs):
    import importlib
    mod = importlib.import_module(module)
    res = None
    if cls is not None:
        mod = getattr(mod, cls)
        if func is None:
            res = mod(*args, **kwargs)

    if not res:
        res = getattr(mod, func)(*args, **kwargs)
    return pickle.dumps(res)  # @app.task(name='create_request')
# def create_request(request: Request):
