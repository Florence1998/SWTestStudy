import pytest


def test_raise():
    with pytest.raises(ValueError, match="must be 0 or None"):  # 预期异常范围为ValueError，并且正则匹配到文字"must be 0 or None"（用的较少），才能通过
        raise ValueError("value must be 0 or None")     # 实际抛出异常为ValueError，在预期范围内，则通过；不在预期范围内就报错


def test_raise1():
    with pytest.raises(ValueError) as exc_info:  # 将捕获到的ValueError异常命名成exc_info
        raise ValueError("value must be 42")
    assert exc_info.type is ValueError  # 通过.type属性来获取到ValueError的异常类型，然后断言是否和ValueError相等
    assert exc_info.value.args[0] == "value must be 42" # 通过.value.args[0]属性来获取到ValueError的打印信息，然后断言是否和"value must be 42"相等
