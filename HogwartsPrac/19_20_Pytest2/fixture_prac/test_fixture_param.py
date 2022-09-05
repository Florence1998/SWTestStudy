import pytest


@pytest.fixture(params=[["selenium", 123], ["appium", 123456]])
def login(request):  # request是不能变的，是内置参数
    print(f"用户名:{request.param}")  # 想拿到每一个参数用"request.param"
    return request.param


def test_demo1(login):
    print(f"demo1 case:数据为{login}")
