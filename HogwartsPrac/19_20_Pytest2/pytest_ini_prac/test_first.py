import logging


# content of test_sample.py
def inc(x):  # 该函数用来完成+1的功能
    return x + 1


def test_answer():
    logging.info("这是answer测试用例")
    logging.info("断言assert inc(4) == 5")
    assert inc(4) == 5


class TestDemo:
    def test_demo1(self):
        logging.info("这是demo1测试用例")
        pass

    def test_demo2(self):
        logging.info("这是demo2测试用例")
        pass
