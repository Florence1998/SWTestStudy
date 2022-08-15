"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

# 使pytest 支持中文
# 收集完测试用例的时候执行的hook函数
import pytest

from pytest_practice.test.utils.log_util import logger


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


# 清理测试数据
# autouse 自动执行
# scope : 作用域
# yield 前相当于setup yield 后相当于teardown
@pytest.fixture(autouse=True, scope="session")
def clear_datas():
    yield
    # teardown
    logger.info("清理所有的测试数据>>>")
