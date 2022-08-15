"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 这个模块 专门用来测试相加方法
# pip install pytest
import pytest
from pytest_practice.test.base.base import Base


def teardown_module():
    # 清理数据
    print("结束测试")


class TestAdd(Base):

    @pytest.mark.P0
    def test_add1(self):
        # result 实际
        result = self.cal.add(1, 1)
        expect = 2
        assert result == expect

    @pytest.mark.P0
    def test_add2(self):
        # result 实际
        result = self.cal.add(-0.01, 0.02)
        expect = 0.01
        assert result == expect

    @pytest.mark.P0
    def test_add3(self):
        # result 实际
        result = self.cal.add(10, 0.02)
        expect = 10.02
        assert result == expect

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
    @pytest.mark.run(order=3)
    def test_add_P1(self):
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
    def test_add12(self):
        # try:
        #     result = self.cal.add("文", 9.3)
        #     # raise NoSuchElementException()
        # except TypeError as e:
        #     print(e)
        with pytest.raises(TypeError) as e:
            result = self.cal.add("文", 9.3)
