import pytest

# 定义了登录的fixture，尽量避免以test_开头
"""
def fixture_name():
    setup操作
    yield 返回值
    teardown操作
"""


@pytest.fixture(scope="class")
def login():
    # setup操作
    print("完成登录操作")
    token = "dadhidfoiahweq"
    username = "hogwarts"
    yield token, username  # 相当于return（直接用return，有返回值，但下方teardown操作不执行）（只写yield，返回None）
    # teardown操作
    print("完成登出操作")


def test_search(login):
    token, username = login
    print(f"token:{token},name:{username}")
    print("搜索")


def test_cart(login):  # 传入login参数，就会先执行login函数
    print("购物车")


def test_order(login):
    print("下单功能")


class TestDemo:
    def test_case1(self, login):
        print("case1")

    def test_case2(self, login):
        print("case2")
