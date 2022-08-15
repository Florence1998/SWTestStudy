"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

from pytest_practice.script.calculator import Calculator
from pytest_practice.test.utils.log_util import logger


class Base:
    def setup_class(self):
        # 类级别  类里的用例只执行一次
        logger.info("实例化 calc 对象 ")
        self.cal = Calculator()

    def setup(self):
        # 每条用例执行一次
        # sleep(1)
        logger.info("开始计算")

    def teardown(self):
        logger.info("结束计算")
