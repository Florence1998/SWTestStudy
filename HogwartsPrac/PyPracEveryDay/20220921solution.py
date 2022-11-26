"""
给定一个n * m 的矩阵 carrot , carrot[i][j] 表示(i, j) 坐标上的胡萝卜数量。从矩阵的中心点出发，每一次移动都朝着四个方向中胡萝卜数量最多的方向移动，保证移动方向唯一。返回你可以得到的胡萝卜数量。

n 和 m 的长度范围是: [1, 300]
carrot[i][j] 的取值范围是: [1, 20000]
中心点是向下取整, 例如n = 4, m = 4, start point 是 (1, 1)
如果格子四周都没有胡萝卜则停止移动
样例
示例 1:

输入:
carrot =
[[5, 7, 6, 3],
[2,  4, 8, 12],
[3, 5, 10, 7],
[4, 16, 4, 17]]
输出:
83
解释：
起点坐标是(1, 1), 移动路线是：4 -> 8 -> 12 -> 7 -> 17 -> 4 -> 16 -> 5 -> 10
题目难度：一般
题目来源：LintCode 炼码 8

示例 2:
输入:
carrot =
[[5, 3, 7, 1, 7],
 [4, 6, 5, 2, 8],
 [2, 1, 1, 4, 6]]
 输出:
 30
 解释：
 起始点是 (1, 2), 移动路线是： 5 -> 7 -> 3 -> 6 -> 4 -> 5
"""


def solution(carrot: list) -> int:
    n = len(carrot) - 1
    m = len(carrot[1]) - 1
    sum_num = (n + 1) * (m + 1)
    i = n // 2
    j = m // 2
    final_road_list = [carrot[i][j]]
    for num in range(0, sum_num):
        road_list = []
        if n >= i - 1 >= 0 and m >= j >= 0:
            road_list.append(carrot[i - 1][j])
        if n >= i + 1 >= 0 and m >= j >= 0:
            road_list.append(carrot[i + 1][j])
        if n >= i >= 0 and m >= j - 1 >= 0:
            road_list.append(carrot[i][j - 1])
        if n >= i >= 0 and m >= j + 1 >= 0:
            road_list.append(carrot[i][j + 1])
        if max(road_list) == 0:
            break
        if n >= i - 1 >= 0 and carrot[i - 1][j] == max(road_list):
            carrot[i][j] = 0
            i = i - 1
            final_road_list.append(carrot[i][j])
        elif n >= i + 1 >= 0 and carrot[i + 1][j] == max(road_list):
            carrot[i][j] = 0
            i = i + 1
            final_road_list.append(carrot[i][j])
        elif m >= j - 1 >= 0 and carrot[i][j - 1] == max(road_list):
            carrot[i][j] = 0
            j = j - 1
            final_road_list.append(carrot[i][j])
        elif m >= j + 1 >= 0 and carrot[i][j + 1] == max(road_list):
            carrot[i][j] = 0
            j = j + 1
            final_road_list.append(carrot[i][j])
    return sum(final_road_list)


carrot = [[5, 7, 6, 3],
          [2, 4, 8, 12],
          [3, 5, 10, 7],
          [4, 16, 4, 17]]
assert solution(carrot) == 83
carrot = [[5, 3, 7, 1, 7],
          [4, 6, 5, 2, 8],
          [2, 1, 1, 4, 6]]
assert solution(carrot) == 30
