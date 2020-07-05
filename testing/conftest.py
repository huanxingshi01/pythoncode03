from typing import List

import pytest
import yaml


@pytest.fixture(scope='function', autouse='True')
def preposition():
    print("开始计算")
    yield
    print("计算结束")


# 自定义hook函数可以将收集上来的测试用例进行改写
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 设置用例显示顺序为倒序
    items.reverse()

    # 设置用例名称可以显示中文
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

    # 自动添加标签
    if 'add' in item.nodeid:
        item.add_marker(pytest.mark.add)
    elif 'div' in item.nodeid:
        item.add_marker(pytest.mark.divs)


def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env", default='test', dest='env', help='set your run env')


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        print("获取测试数据")
        with open("data/testdatas/test/test.yaml") as f:
            datas = yaml.safe_load(f)
    elif myenv == 'dev':
        print("获取dev数据")
        with open("data/testdatas/dev/dev.yaml") as f:
            datas = yaml.safe_load(f)
    elif myenv == 'st':
        print("获取st数据")
        with open("data/testdatas/st/st.yaml") as f:
            datas = yaml.safe_load(f)
    return datas
