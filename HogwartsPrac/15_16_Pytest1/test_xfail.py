import pytest


def test_xfail():
    print("***开始测试***")
    pytest.xfail(reason="该功能尚未完成")  # 执行到这下面就不会执行了
    print("测试过程")
    assert 1 == 1

# @pytest.mark.xfail
# def test_aaa():
#     print("test_xfail1 方法执行")
#     assert 2 == 2
#
#
# xfail = pytest.mark.xfail
#
#
# @xfail(reason="bug 110")
# def test_hello():
#     assert 0
