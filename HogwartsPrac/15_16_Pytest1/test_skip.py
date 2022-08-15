import sys
import pytest

print(sys.platform)


@pytest.mark.skipif(sys.platform == "darwin", reason="does not run on mac")
def test_case1():
    assert True


@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows32")
def test_case2():
    assert True


@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
def test_case3():
    assert True


# # 代码中添加 跳过代码块 pytest.skip(reason="")
# def check_login():
#     return False
#
#
# def test_function():
#     print("start")
#     # 如果未登录，则跳过后续步骤
#     if not check_login():
#         pytest.skip("unsupported configuration")
#     print("end")


# @pytest.mark.skip
# def test_aaa():
#     print("start")
#     assert True
#
#
# @pytest.mark.skip(reason="代码没有实现")
# def test_bbb():
#     assert False


# if not sys.platform.startswith("darwin"):
#     pytest.skip("skipping windows_only tests", allow_moudule_level=True)
