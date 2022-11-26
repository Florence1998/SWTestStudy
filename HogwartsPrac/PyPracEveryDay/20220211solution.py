"""
给定一个由纯数字组成的字符串，每个数字之间使用空格分隔。我们的任务是，编写一个函数，找出其中最大和最小的两个数字。返回结果的两个数字格式为字符串，并且逆序排列，也使用空格分隔。

示例：
输入：1 2 3 4 5，输出：5 1。

题目难度：简单
题目来源：CodeWars: Highest and Lowest 17

def solution(nums: str) -> str:
    # your code here

assert solution("1 2 3 4 5") == "5 1"
assert solution("1 2 -3 4 5") == "5 -3"
assert solution("1 9 3 4 -5") == "9 -5"
assert solution("1 2 3") == "3 1"
assert solution("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9"
"""


def solution(nums: str) -> str:
    nums_list = nums.split(" ")
    nums_list_int = []
    for i in nums_list:
        nums_list_int.append(int(i))
    return " ".join([str(max(nums_list_int)), str(min(nums_list_int))])


assert solution("1 2 3 4 5") == "5 1"
assert solution("1 2 -3 4 5") == "5 -3"
assert solution("1 9 3 4 -5") == "9 -5"
assert solution("1 2 3") == "3 1"
assert solution("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9"
