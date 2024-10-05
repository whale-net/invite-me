import pickle

import pytest

from invite_me.executors import LocalExecutor, CeleryExecutor


@pytest.fixture(scope="package", params=[LocalExecutor, CeleryExecutor])
def local_executor(request):
    yield request.param()


def _test_function(a: int, b: int) -> int:
    return a + b


def test_instantiation(executor):
    res = executor.execute_static(module="invite_me.tests.test_executor", func="_test_function", a=1, b=2)
    unpickled = pickle.loads(res)
    assert type(unpickled) == int
    assert unpickled == 3
