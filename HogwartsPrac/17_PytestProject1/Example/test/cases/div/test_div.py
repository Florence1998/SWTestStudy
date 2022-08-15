"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import allure
import pytest

from pytest_practice.test.base.base import Base


# 继承Base里所有的方法
# 大的分类 feature
# 小的分类 story
@allure.feature("相除功能")
class TestDiv(Base):
    @pytest.mark.P0
    @pytest.mark.parametrize('a,b,expect', [[1, 1, 1],
                                            [-0.01, -0.02, 0.5],
                                            [-0.01, 0.02, -0.5],
                                            [10, 0.02, 500],
                                            ],
                             ids=["2个整数", "2个负浮点数", "2w个浮点数-正负", "整数和浮点数"])
    @pytest.mark.run(order=2)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @allure.story("P0级别")
    def test_div_P0(self, a, b, expect):
        """
        :return:
        """
        with allure.step("step1: 相除操作"):
            result = self.cal.div(a, b)
        with allure.step("step2: 出错截图"):
            allure.attach.file(
                "/Users/juanxu/Documents/霍格沃兹测试学院/03ceshiren实战项目代码/hogwarts-pytest-prac24/test/img/logo.jpg",
                name="截图", attachment_type=allure.attachment_type.JPG)
        with allure.step("step3: 断言结果"):
            assert result == expect

    # def test_div2(self):
    #     datas = [[1,1,1],
    #              [-0.01,-0.02,0.51],
    #             [-0.01,0.02,-0.5],
    #              [10,0.02,500],]
    #     # 问题：一旦其中某一条数据对应的用例错误 ，后面的测试数据将不再被执行
    #     for data in datas:
    #         result = self.cal.div(data[0], data[1])
    #         assert result == data[2]

    @pytest.mark.P1
    @pytest.mark.run(order=-1)
    @pytest.mark.parametrize('a,b,expect', [[99, 0, "ZeroDivisionError"]], ids=["除数为0"])
    def test_div_P1(self, a, b, expect):
        with pytest.raises(eval(expect)) as e:
            result = self.cal.div(a, b)
