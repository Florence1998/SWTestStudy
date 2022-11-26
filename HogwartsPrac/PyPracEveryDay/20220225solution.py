"""
已知一个包含唯一数字的列表，和一个指定的左闭右开区间[from, to)，我们的任务是：首先凑对，找出存在几对元素之和在区间内，然后将这些符合区间的和加总得到最终的和值。

备注：

所有凑对的元素必须是唯一的
凑对的和值只在区间内统计一次
示例：
已知列表是 [2, 4, 6, 10]，已知区间是[6， 10)

6：可以等于 2 + 4
7：无法凑对
8：可以等于 2 + 6
9：无法凑对

最终结果：6 + 8 = 14

题目难度：中等
题目来源：CodeWars： 2-Sum Sums 9

def solution(nums: list, target: range) -> int:
    # your code here

assert solution([2, 4, 6, 10], range(6, 10)) == 14
"""


def solution(nums: list, target: range) -> int:
    res_list = []
    for i in nums:
        for j in nums:
            if nums.index(i) >= nums.index(j):
                continue
            if i + j in target:
                res_list.append(i + j)
    return sum(res_list)


assert solution([2, 4, 6, 10], range(6, 10)) == 14
