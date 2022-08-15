# 这个模块 专门用来测试相加方法
# 1、安装pytest第三方库：pip install pytest
# 2、Pycharm设置默认测试执行器为Pytest
import pytest

from script.calculator import Calculator


def teardown_module():
    # 清理数据
    print("【结束测试】")


class TestAdd(object):
    def setup(self):
        print("【开始计算】")

    def teardown(self):
        print("【结束计算】")


    test_case_list =[(1,1,2),(-0.01,0.02,0.01),(10,0.02,10.02)]
    @pytest.mark.P0
    @pytest.mark.parametrize()
    def test_add1(self,"input1,input2,expect",test_case_list):
        self.cal = Calculator()
        # result 实际结果
        result = self.cal.add(input1, input2)
        # expect 预期结果
        assert result == expect

    @pytest.mark.P0
    def test_add2(self):
        self.cal = Calculator()
        # result 实际结果
        result = self.cal.add(-0.01, 0.02)
        # expect 预期结果
        expect = 0.01
        assert result == expect
