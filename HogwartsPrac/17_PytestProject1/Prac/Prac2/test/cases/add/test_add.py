# 这个模块 专门用来测试相加方法
# 1、安装pytest第三方库：pip install pytest
# 2、Pycharm设置默认测试执行器为Pytest
import pytest
from script.calculator import Calculator
from test.base.base import Base


def teardown_module():
    # 清理数据
    print("【结束测试】")


class TestAdd(Base):  # 继承base.py的Base类
    # test_case_list =[(1,1,2),(-0.01,0.02,0.01),(10,0.02,10.02)]
    # @pytest.mark.P0
    # @pytest.mark.parametrize()
    # def test_add1(self,"input1,input2,expect",test_case_list):
    #     # result 实际结果
    #     result = self.cal.add(input1, input2)
    #     # expect 预期结果
    #     assert result == expect

    @pytest.mark.P0
    def test_add1(self):
        # result 实际结果
        result = self.cal.add(1, 1)
        # expect 预期结果
        expect = 2
        assert result == expect

    @pytest.mark.P0
    def test_add2(self):
        # result 实际结果
        result = self.cal.add(-0.01, 0.02)
        # expect 预期结果
        expect = 0.01
        assert result == expect

    @pytest.mark.P0
    def test_add3(self):
        # result 实际结果
        result = self.cal.add(10, 0.02)
        # expect 预期结果
        expect = 10.02
        assert result == expect

    @pytest.mark.P1
    def test_add4(self):
        # result 实际结果
        result = self.cal.add(98.99, 99)
        # expect 预期结果
        expect = 197.99
        assert result == expect

    @pytest.mark.P1
    def test_add5(self):
        # result 实际结果
        result = self.cal.add(99, 98.99)
        # expect 预期结果
        expect = 197.99
        assert result == expect

    @pytest.mark.P1
    def test_add6(self):
        # result 实际结果
        result = self.cal.add(-98.99, -99)
        # expect 预期结果
        expect = -197.99
        assert result == expect

    @pytest.mark.P1
    def test_add7(self):
        # result 实际结果
        result = self.cal.add(-99, -98.99)
        # expect 预期结果
        expect = -197.99
        assert result == expect

    @pytest.mark.P1
    def test_add8(self):
        # result 实际结果
        result = self.cal.add(99.01, 0)
        # expect 预期结果
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.P1
    def test_add9(self):
        # result 实际结果
        result = self.cal.add(-99.01, -1)
        # expect 预期结果
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.P1
    def test_add10(self):
        # result 实际结果
        result = self.cal.add(2, 99.01)
        # expect 预期结果
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.P1
    def test_add11(self):
        # result 实际结果
        result = self.cal.add(1, -99.01)
        # expect 预期结果
        expect = "参数大小超出范围"
        assert result == expect

    @pytest.mark.P1
    def test_add12(self):
        # result 实际结果
        # try:
        #     result = self.cal.add("文", 9.3)  # 捕获的异常TypeError和被抛出的异常TypeError一样，不会报错
        #     # raise NoSuchElementException()  # 捕获的异常TypeError和被抛出的异常NoSuchElementException不一样，会报错
        # # expect 预期结果
        # except TypeError as e:
        #     print(e)
        with pytest.raises(TypeError):
            result = self.cal.add("文", 9.3)
