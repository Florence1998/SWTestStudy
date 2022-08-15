"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 这个模块 专门用来测试相加方法
# pip install pytest
import allure
import pytest

from pytest_practice.test.base.base import Base
from pytest_practice.test.utils.log_util import logger


def teardown_module():
    # 清理数据
    print("结束测试")


# 安装 java
# 安装 allure
# 安装 allure-pytest
@allure.feature("相加功能")
class TestAdd(Base):

    @allure.story("相加P0级别用例")
    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect", [[1, 1, 2],
                                            [-0.01, 0.02, 0.01],
                                            [10, 0.02, 10.02]
                                            ],
                             ids=["int", "float", "int_float"])
    # 参数化，当测试步骤完全一样， 测试数据不一样的时候就可以使用参数化
    def test_add1(self, a, b, expect):
        # result 实际
        logger.info(f"输入数据：{a},{b}，期望结果：{expect}")
        with allure.step("step1:相加操作"):
            result = self.cal.add(a, b)
        logger.info(f"实际结果：{result}")
        # expect = 2
        # allure.attach.file("/Users/juanxu/Documents/霍格沃兹测试学院/01ceshiren实战项目/HogwartsPytestPrac24/test/img/logo.jpg",
        #                    name="计算完成截图")
        allure.attach.file("/Users/juanxu/Documents/霍格沃兹测试学院/03ceshiren实战项目代码/hogwarts-pytest-prac24/test/img/logo.jpg",
                           name="截图",
                           attachment_type=allure.attachment_type.JPG,
                           )
        with allure.step("step2:断言"):
            assert result == expect

    @allure.story("相加P1级别用例")
    @pytest.mark.P1
    def test_add4(self):
        # result 实际
        result = self.cal.add(98.99, 99)
        expect = 197.99
        assert result == expect

    @pytest.mark.P1
    def test_add5(self):
        # result 实际
        result = self.cal.add(99, 98.99)
        expect = 197.99
        assert result == expect

    @pytest.mark.P1
    def test_add6(self):
        # result 实际
        result = self.cal.add(-98.99, -99)
        expect = -197.99
        assert result == expect

    @pytest.mark.P1
    def test_add7(self):
        # result 实际
        result = self.cal.add(-99, -98.99)
        expect = -197.99
        assert result == expect

    @pytest.mark.P1
    def test_add8(self):
        # result 实际
        result = self.cal.add(99.01, 0)
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.P1
    def test_add9(self):
        # result 实际
        result = self.cal.add(-99.01, -1)
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.P1
    def test_add10(self):
        # result 实际
        result = self.cal.add(2, 99.01)
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.P1
    def test_add11(self):
        # result 实际
        result = self.cal.add(1, -99.01)
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.P1
    @pytest.mark.parametrize("a,b,expect", [["文", 9.3, "TypeError"]],
                             ids=["chinese"])
    def test_add12(self, a, b, expect):
        # try:
        #     result = self.cal.add("文", 9.3)
        #     # raise NoSuchElementException()
        # except TypeError as e:
        #     print(e)
        with pytest.raises(eval(expect)) as e:
            result = self.cal.add(a, b)
