"""
假设我们有一个拥有8个方位的罗盘（N, NE, E, SE, S, SW, W, NW），再给定一个需要转动的角度（45度的倍数），请 编写一个函数，求出转动后的角度。转动角度可以是正数，也可以是负数。

【示例】
输入：“S”, 180
输出：“N”
解释：S 表示正南，旋转180度后，就会指向正北，即 N

题目难度：简单
题目来源：CodeWars-Turn with a Compass 12

def solution(direction: str, degree: int)-> str:
    # your code here

assert solution("S", 180) == "N"
assert solution("SE", -45) == "E"
assert solution("W",  495) == "NE"
"""


def solution(direction: str, degree: int) -> str:
    direction_list = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    if degree % 45 == 0:
        res_index = (degree // 45 + direction_list.index(direction)) % 8
        return direction_list[res_index]
    else:
        return False


assert solution("S", 180) == "N"
assert solution("SE", -45) == "E"
assert solution("W", 495) == "NE"
