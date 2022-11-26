"""
一个数字的真除数是除了自身之外的所有整除数的集合。例如，对于100，它们是1、2、4、5、10、20、25和50。

设s（n）是n的这些真除数之和。将buddy称为两个正整数，这样每个数的真除数的和比另一个数多一个：（n，m）是一对伙伴，如果s（m）=n+1和s（n）=m+1

例如，48和75就是这样一对：

48的除数是：1、2、3、4、6、8、12、16、24–>和：76=75+1

75的除数是：1、3、5、15、25–>和：49=48+1

任务

给定两个正整数start和limit，函数buddy（start，limit）应该返回buddy对的第一对（n m），这样n（正整数）就在 start 和 limits 之间；m可以大于极限，并且必须大于n

如果没有满足条件的好友数据对，则返回 “Nothing”

示例

buddy（10，50）返回[48，75]

buddy（48，50）返回[48，75]

题目难度：一般
题目来源： Buddy Pairs II | Codewars 2

from typing import Union

def buddy(start: int, limit: int) -> Union[list, str]:
    # your code here
    return []

assert buddy(10, 50) == [48, 75]
assert buddy(2177, 4357) == "Nothing"
assert buddy(57345, 90061) == [62744, 75495]
assert buddy(1071625, 1103735) == [1081184, 1331967]
"""
from typing import Union


def buddy(start: int, limit: int) -> Union[list, str]:
    i_list = []
    j_list = []
    for n in range(start, limit + 1):
        for i in range(1, n):
            if n % i == 0:
                i_list.append(i)
        sn = sum(i_list)
        i_list = []
        m = sn - 1
        if m <= n:
            continue
        for j in range(1, m):
            if m % j == 0:
                j_list.append(j)
        sm = sum(j_list)
        j_list = []
        if sm == n + 1:
            return [n, m]
        else:
            continue
    return "Nothing"


assert buddy(10, 50) == [48, 75]
assert buddy(2177, 4357) == "Nothing"
assert buddy(57345, 90061) == [62744, 75495]
assert buddy(1071625, 1103735) == [1081184, 1331967]
# assert buddy(62744, 90061) == [62744, 75495]
# assert buddy(1081184, 1103735) == [1081184, 1331967]
