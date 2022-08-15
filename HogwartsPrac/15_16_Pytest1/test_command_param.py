import pytest


def double(a):
    return a * 2


# 测试数据：整型
@pytest.mark.int
def test_double_int():
    print("test double int")
    assert double(1) == 2


# 测试数据：负数
@pytest.mark.minus
def test_double_minus():
    print("test double minus")
    assert double(-1) == -2


# 测试数据：浮点数
@pytest.mark.float
def test_double_float1():
    print("test double float1")
    assert double(0.1) == 0.2


@pytest.mark.float
def test_double_float2():
    print("test double float2")
    assert double(-0.1) == -0.2


# 测试数据：0
@pytest.mark.zero
def test_double_zero():
    print("test double zero")
    assert double(0) == 0


# 测试数据：大数字
@pytest.mark.bignum
def test_double_bignum():
    print("test double bignum")
    assert double(100) == 200


# 测试数据：字符串
@pytest.mark.str
def test_double_str1():
    print("test double str1")
    assert double("a") == "aa"


@pytest.mark.str
def test_double_str2():
    print("test double str2")
    assert double("a$") == "a$a$"

