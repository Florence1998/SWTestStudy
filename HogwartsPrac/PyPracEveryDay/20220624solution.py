"""
如果我们列出所有小于 10 且是 3 或 5 的倍数的自然数，我们会得到 3、5、6 和 9。这些倍数之和是 23。

设计一个方法，使其返回传入数字以下的所有 3 或 5 的倍数之和。此外，如果数字为负数，则返回 0。

注意：如果数字是 3 和 5 的倍数， 则只计算一次。

【示例】
输入：10
输出：23
解释：列出所有小于 10 且是 3 或 5 的倍数的自然数，我们会得到 3、5、6 和 9。这些倍数之和是 23。

题目难度：简单
题目来源：Multiples of 3 or 5 | Codewars 7


def solution(number):
    pass

assert solution(10) == 23
assert solution(-1) == 0
assert solution(15) == 45
assert solution(200) == 9168
"""


def solution(number):
    res_list = []
    for i in range(0, number):
        if (i % 3 == 0) or (i % 5 == 0):
            res_list.append(i)
    return sum(res_list)


assert solution(10) == 23
assert solution(-1) == 0
assert solution(15) == 45
assert solution(200) == 9168
