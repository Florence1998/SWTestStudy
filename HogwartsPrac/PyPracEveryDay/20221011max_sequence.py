"""
子序列最大和，包括在一个数组或整数列表中查找连续子序列的最大和：

最大序列（[-2，1，-3，4，-1，2，1，-5，4]）
应为6:
[4，-1，2，1]

简单的情况是，列表仅由正数组成，最大和是整个数组的和。如果列表仅由负数组成，则返回0。

空列表被视为最大和为零。请注意，空列表或数组也是有效的子列表/子数组。’

题目难度：简单
题目来源： Maximum subarray sum | Codewars 3

def max_sequence(arr: list) -> int:
    # your code here

assert max_sequence([]) == 0
assert max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]) == 0
assert max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]) == 155
assert max_sequence([-6, -3, 27, -22, 3, 8, 19, -7, -26, -30, -3, -26, 22, 25, -26, 27, 4, -24, -7, 20, 20, 20, 9, -23, -26, -27, -12, 0, 1, 26, -19, -1, -15, -16, 1, 25, 4, -7, 27, 4, -22, -10, 23, 4, 2, -29, 0, -12, -21, 7]) == 90
"""


def max_sequence(arr: list) -> int:
    arr_len = len(arr)
    my_list = []
    if arr_len == 0:  # 如果是空列表，返回0
        return 0
    else:
        for i in range(0, arr_len):
            for j in range(i + 1, arr_len + 1):
                my_list.append(sum(arr[i:j]))  # 通过sum求切片和，列举出所有情况
                my_list.sort(reverse=True)  # 对切片和所有情况排序，找最大值
        if my_list[0] <= 0:  # 如果最大值小于等于0（全负数情况），返回0
            return 0
        else:
            return int(my_list[0])  # 输出最大值


assert max_sequence([]) == 0
assert max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]) == 0
assert max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]) == 155
assert max_sequence(
    [-6, -3, 27, -22, 3, 8, 19, -7, -26, -30, -3, -26, 22, 25, -26, 27, 4, -24, -7, 20, 20, 20, 9, -23, -26, -27, -12,
     0, 1, 26, -19, -1, -15, -16, 1, 25, 4, -7, 27, 4, -22, -10, 23, 4, 2, -29, 0, -12, -21, 7]) == 90
