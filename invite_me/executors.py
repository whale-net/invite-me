import pickle
from abc import ABC, abstractmethod
from typing import Optional, Any

from invite_me import _celery


class Executor(ABC):

    @abstractmethod
    def execute_static(self, module: str, cls: Optional[str], func: Optional[str] = None, *args, **kwargs) -> Any:
        pass

    def init_class(self, module: str, cls: str, *args, **kwargs):
        return self.execute_static(module=module, cls=cls, *args, **kwargs)

    @abstractmethod
    def execute_obj(self, obj: Any, func: str, *args, **kwargs) -> Any:
        pass


class CeleryExecutor(Executor):
    def execute_obj(self, obj, func, *args, **kwargs):
        task = _celery.app.send_task(name='execute_obj',
                                     args=args,
                                     kwargs={"obj": pickle.dumps(obj), "func": func, **kwargs})
        return pickle.loads(task.get(timeout=5))

    def execute_static(self, module: str, cls: Optional[str] = None, func: Optional[str] = None, *args,
                       **kwargs) -> Any:
        task = _celery.app.send_task(name='execute_static',
                                     args=args,
                                     kwargs={"module": module, "cls": cls, "func": func, **kwargs})  # Send task by name
        return pickle.loads(task.get(timeout=5))


class LocalExecutor(Executor):
    def __init__(self):
        pass

    def execute_static(self, module: str, cls: Optional[str] = None, func: Optional[str] = None, *args, **kwargs):
        import importlib
        mod = importlib.import_module(module)
        res = None
        if cls is not None:
            mod = getattr(mod, cls)
            if func is None:
                res = mod(*args, **kwargs)

        if not res:
            res = getattr(mod, func)(*args, **kwargs)
        return res

    def execute_obj(self, obj, func, *args, **kwargs):
        return getattr(obj, func)(*args, **kwargs)
