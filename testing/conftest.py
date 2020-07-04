import pytest


@pytest.fixture(scope='function', autouse='True')
def preposition():
    print("开始计算")
    yield
    print("计算结束")
