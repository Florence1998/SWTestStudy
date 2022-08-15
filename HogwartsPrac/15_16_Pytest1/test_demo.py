import sys


def test_plat():
    assert ("win32" in sys.platform), "该代码只能在Linux下执行"


class TestDemo(object):
    def test_demo1(self):
        pass
