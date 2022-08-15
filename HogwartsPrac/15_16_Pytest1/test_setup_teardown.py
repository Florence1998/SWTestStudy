"""
模块级(setup_module/teardown_module)模块始末，全局的（优先最高)
函数级(setup_function/teardown_function)只对函数用例生效(不在类中)
类级(setup_class/teardown_class)只在类中前后运行一次(在类中)
方法级(setup_method/teardown_method)开始于方法始末(在类中)
类里面的(setup/teardown)运行在调用方法的前后
"""


# 模块级别，只被调用一次
def setup_module():
    print("资源准备：setup module")


def teardown_module():
    print("资源销毁：teardown module")


# 函数1
def test_case1():
    print("case1")


# 函数2
def test_case2():
    print("case2")


# 函数级别
def setup_function():
    print("资源准备：setup function")


def teardown_function():
    print("资源销毁：teardown function")


class TestDemo(object):
    # 每个类里面的方法前后分别执行setup、teardown
    def setup(self):
        print("TestDemo资源准备：setup")

    def teardown(self):
        print("TestDemo资源销毁：teardown")

    # def setup_method(self):
    #     print("TestDemo资源准备：setup method")
    #
    # def teardown_method(self):
    #     print("TestDemo资源销毁：teardown method")
    # 方法1
    def test_demo1(self):
        print("demo1")

    # 方法2
    def test_demo2(self):
        print("demo2")
