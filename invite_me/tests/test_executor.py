import pytest

from invite_me.executors import LocalExecutor, CeleryExecutor


@pytest.fixture(scope="package", params=[LocalExecutor, CeleryExecutor])
def executor(request):
    yield request.param()


def _test_function(a: int, b: int) -> int:
    return a + b


class EchoClass:
    @staticmethod
    def test_echo_func(x):
        return x

    def __init__(self, x):
        self._x = x
        pass

    def get_x(self):
        return self._x


def test_function(executor):
    res = executor.execute_static(module="invite_me.tests.test_executor", func="_test_function", a=1, b=2)
    assert isinstance(res, int)
    assert res == 3


def test_static_class_function(executor):
    res = executor.init_class(module="invite_me.tests.test_executor", cls="EchoClass", x=1)
    assert isinstance(res, EchoClass)
    assert res.get_x() == 1

    res = executor.execute_static(module="invite_me.tests.test_executor", cls="EchoClass", func="test_echo_func",
                                  x={"id": 123})
    assert isinstance(res, dict)
    assert res["id"] == 123


def test_obj_func(executor):
    x = executor.execute_static("invite_me.tests.test_executor", cls="EchoClass",
                                x={"something": "else"})
    assert executor.execute_obj(x, "get_x")["something"] == "else"
