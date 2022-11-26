"""
给定一个整数n，通过移除其中某一位数字，找出操作之后遗留的最大数字。

【示例】
输入：152
输出：52
解释：如果移除1，得到52；如果移除5，得到12；如果移除2，得到15。因此最大方案是移除1得到52。

题目难度：中等
题目来源：Simple Fun #79: Delete a Digit 9

def solution(n: int)-> int:
    # your code here

assert solution(152) == 52
assert solution(1001) == 101
assert solution(10) == 1
"""


def solution(n: int) -> int:
    str_n = str(n)
    res = []
    for i in range(0, len(str_n)):
        res.append(str_n.replace(str_n[i], "", 1))
    return int(max(res))


assert solution(152) == 52
assert solution(1001) == 101
assert solution(10) == 1
