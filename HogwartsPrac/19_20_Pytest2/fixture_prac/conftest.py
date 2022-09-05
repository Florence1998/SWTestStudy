# conftest.py名字是固定的，不能改变
import pytest


@pytest.fixture(scope="function", autouse=True)
def login():
    # setup操作
    print("完成登录操作")
    token = "dadhidfoiahweq"
    username = "hogwarts"
    yield token, username  # 相当于return（直接用return，有返回值，但下方teardown操作不执行）（只写yield，返回None）
    # teardown操作
    print("完成登出操作")


@pytest.fixture()  # 每个方法都要加fixture装饰器
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库")
