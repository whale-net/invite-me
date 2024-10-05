from abc import ABC, abstractmethod
from typing import Optional, Any

from invite_me import _celery


class Executor(ABC):
    @abstractmethod
    def execute_static(self, module: str, cls: Optional[str], func: Optional[str] = None, *args, **kwargs) -> Any:
        pass

    def init_class(self, module, cls, *args, **kwargs):
        return self.execute_static(module=module, cls=cls, *args, **kwargs)

    @abstractmethod
    def execute_obj(self, obj, func, *args, **kwargs) -> Any:
        pass


class CeleryExecutor(Executor):
    def execute_obj(obj, func, *args, **kwargs):
        pass

    def __init__(self):
        pass

    def execute_static(self, module: str, cls: Optional[str] = None, func: Optional[str] = None, *args,
                       **kwargs) -> bytes:
        task = _celery.app.send_task('execute_static', ['invite_me.tmp'], args=args, kwargs=kwargs)  # Send task by name
        return task


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
