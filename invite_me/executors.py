import pickle
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from invite_me import _celery


@dataclass
class ExecutionResult:
    data: bytes


class Executor(ABC):
    @abstractmethod
    def execute_static(self, module: str, cls: Optional[str], func: Optional[str] = None, *args, **kwargs) -> bytes:
        pass


class CeleryExecutor(Executor):
    def __init__(self):
        pass

    def execute_static(self, module: str, cls: Optional[str] = None, func: Optional[str] = None, *args,
                       **kwargs) -> bytes:
        task = _celery.app.send_task('execute_static', ['invite_me.tmp'])  # Send task by name
        return task


class LocalExecutor(Executor):
    def __init__(self):
        pass

    def execute_static(self, module: str, cls: Optional[str] = None, func: Optional[str] = None, *args, **kwargs):
        import importlib
        mod = importlib.import_module(module)
        res = getattr(mod, func)(*args, **kwargs)
        return pickle.dumps(res)
