import pickle
from abc import ABC, abstractmethod
from typing import Optional, Any

from invite_me.tasks import execute_static, execute_obj


class Executor(ABC):
    @abstractmethod
    def execute_static(
        self,
        module: str,
        cls: Optional[str],
        func: Optional[str] = None,
        *args,
        **kwargs,
    ) -> Any:
        """Execute a static method by name"""
        pass

    def init_class(self, module: str, cls: str, *args, **kwargs):
        return self.execute_static(module=module, cls=cls, *args, **kwargs)

    @abstractmethod
    def execute_obj(self, obj: Any, func: str, *args, **kwargs) -> Any:
        pass


class CeleryExecutor(Executor):
    def __init__(self, celery_app):
        self._celery_app = celery_app

    def execute_obj(self, obj, func, *args, **kwargs):
        """
        Kicks off execute_obj in a celery worker.

        Uses pickle to provide an object to celery, to invoke a function of with arguments.

        :param obj: Object to use.
        :param func: Method of obj to invoke.
        :param args: args of func.
        :param kwargs: kwargs of func.
        :return: Un-pickled result of func.
        """
        task = self._celery_app.send_task(
            name="execute_obj",
            args=args,
            kwargs={"obj": pickle.dumps(obj), "func": func, **kwargs},
        )
        return pickle.loads(task.get(timeout=5))

    def execute_static(
        self,
        module: str,
        cls: Optional[str] = None,
        func: Optional[str] = None,
        *args,
        **kwargs,
    ) -> Any:
        """
        Kicks off execute_static in a celery worker.

        :param module: The module which contains the method to invoke. If cls and func aren't provided, the module will be ran.
        :param cls: The class to import or execute.
        :param func: The function to execute
        :param args:
        :param kwargs:
        :return:
        """
        task = self._celery_app.send_task(
            name="execute_static",
            args=args,
            kwargs={"module": module, "cls": cls, "func": func, **kwargs},
        )  # Send task by name
        return pickle.loads(task.get(timeout=5))


class LocalExecutor(Executor):
    """
    Primarily exists for the purpose of testing. Calls the same methods celery does, but without being connected
    to the celery channel. Will still pickle and unpickle the object.
    """

    def __init__(self):
        pass

    def execute_static(
        self,
        module: str,
        cls: Optional[str] = None,
        func: Optional[str] = None,
        *args,
        **kwargs,
    ):
        return pickle.loads(
            execute_static(module=module, cls=cls, func=func, *args, **kwargs)
        )

    def execute_obj(self, obj, func, *args, **kwargs):
        return pickle.loads(
            execute_obj(obj=pickle.dumps(obj), func=func, *args, **kwargs)
        )
