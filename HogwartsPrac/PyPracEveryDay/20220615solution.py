"""
给定一个字符串列表，请根据每个元素的出现顺序进行编号，从1开始，返回编号后的字符串列表。编号元素的格式是：序号:元素。

【示例】
输入：["a", "b", "c"]
输出：["1: a", "2: b", "3: c"]
解释：a的序号是1，b的序号是2，c的序号是3。

题目难度：简单
题目来源：codewars-Testing 1-2-3 9

def solution(msg: list)-> list:
    # your code here

assert solution([]) == []
assert solution(["a", "b", "c"]) == ["1:a", "2:b", "3:c"]
"""


def solution(msg: list) -> list:
    msg_index = 1
    res_list = []
    for i in msg:
        res_list.append(str(msg_index) + ":" + i)
        msg_index += 1
    return res_list


assert solution([]) == []
assert solution(["a", "b", "c"]) == ["1:a", "2:b", "3:c"]
