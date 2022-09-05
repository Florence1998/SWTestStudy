import pytest


@pytest.fixture()
def login():
    print("完成登录操作")


def test_search(login):
    print("搜索")


def test_cart(login):  # 传入login参数，就会先执行login函数
    print("购物车")


def test_order(login):
    print("下单功能")
