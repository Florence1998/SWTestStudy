# content of test_sample.py
def inc(x):  # 该函数用来完成+1的功能
    return x + 1


def test_answer():  # 该函数对inc(x)函数进行一个验证
    assert inc(4) == 5  # 通过assert完成一个断言（数据结果的校验）


class TestDemo(object):
    def test_demo1(self):
        print("日志信息1")
        pass

    def test_demo2(self):
        print("日志信息2")
        pass
