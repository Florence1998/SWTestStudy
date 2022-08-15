import pytest

test_case_list = [("3+5", 8), ("2+5", 7), ("7+5", 12)]  # 参数的值我们可以放在列表或元组里面


# 1、参数化的名字，要与方法中的参数名，一一对应
# 2、如果传递多个参数的话，要放在列表中，列表中嵌套列表/元组
# 3、ids的个数 == 传递数据的个数
@pytest.mark.parametrize("test_input, expected", test_case_list, ids=["num1", "num2", "num3"])  # 参数的名字test_input, expected放在第一个位置，有哪些参数放在第二个位置
def test_mark_more(test_input, expected):  # 传递test_input, expected两个参数
    assert eval(test_input) == expected
