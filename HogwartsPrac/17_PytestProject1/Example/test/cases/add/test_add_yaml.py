"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import allure
import pytest

from pytest_practice.test.base.base import Base
from pytest_practice.test.utils.log_util import logger
from pytest_practice.test.utils.util import get_adddata


@allure.feature("相加功能")
class TestAdd(Base):
    add_P0_data = get_adddata("add", "P0")[0]
    add_P0_ids = get_adddata("add", "P0")[1]

    @allure.story("相加P0级别用例")
    @pytest.mark.run(order=1)
    @pytest.mark.P0
    # @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @pytest.mark.parametrize("a,b,expect", add_P0_data, ids=add_P0_ids)
    # 参数化，当测试步骤完全一样， 测试数据不一样的时候就可以使用参数化
    def test_add_P0(self, a, b, expect):
        # result 实际
        logger.info(f"输入数据：{a},{b}，期望结果：{expect}")
        with allure.step("step1:相加操作"):
            result = self.cal.add(a, b)
        logger.info(f"实际结果：{result}")
        # expect = 2
        allure.attach.file("/Users/juanxu/Documents/霍格沃兹测试学院/03ceshiren实战项目代码/hogwarts-pytest-prac24/test/img/logo.jpg",
                           name="截图",
                           attachment_type=allure.attachment_type.JPG,
                           )
        with allure.step("step2:断言"):
            assert result == expect
