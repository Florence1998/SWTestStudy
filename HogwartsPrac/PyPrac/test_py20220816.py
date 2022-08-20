"""
完成解决方案，以便将字符串拆分为两个字符对。如果字符串包含奇数个字符，则应将最后一对中缺少的第二个字符替换为下划线 (’_’) 。

例子：

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
题目难度：简单
题目来源：Split Strings | Codewars

def solution(s: str) -> list:
    # your code here

assert solution("asdfadsf") == ['as', 'df', 'ad', 'sf']
assert solution("asdfads") == ['as', 'df', 'ad', 's_']
assert solution("") == []
assert solution("x") == ['x_']
"""


def solution(s: str) -> list:
    # your code here
    if len(s) % 2 == 0:
        s = list(s)
        n = len(s) - 1
        for i in range(0, n, 2):
            s[i] += s[i + 1]
        s = s[::2]
        return s
    elif len(s) == 0:
        return []
    else:
        s = s + '_'
        return solution(s)


def test_solution():
    assert solution("asdfadsf") == ['as', 'df', 'ad', 'sf']
    assert solution("asdfads") == ['as', 'df', 'ad', 's_']
    assert solution("awsdwerd") == ['aw', 'sd', 'we', 'rd']
    assert solution("") == []
    assert solution("x") == ['x_']
