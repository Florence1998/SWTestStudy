"""
有一天你贡献了一个非常好的idea，老板给了你一笔奖金。为了庆祝，你把你的朋友们带到可怕的潜水酒吧，并使用奖金购买和建造最大的三维啤酒罐金字塔。然后与朋友们进入狂欢。

啤酒罐金字塔建造的规则是：顶层1罐，第二层4罐，下一层9罐，下一层16罐，25罐…

完成 beeramid 函数以返回您可以制作的啤酒罐完整金字塔的层数，给定以下参数：

您的奖金 bonus，以及啤酒的价格 price

例如：

beeramid(1500, 2)  # should === 12
beeramid(5000, 3) # should === 16
题目难度：中等
题目来源：Beeramid | Codewars 4


def beeramid(bonus: float, price: float) -> int:
    # your code here

assert beeramid(9, 2) == 1
assert beeramid(10, 2) == 2
assert beeramid(11, 2) == 2
assert beeramid(21, 1.5) == 3
assert beeramid(454, 5) == 5
assert beeramid(455, 5) == 6
assert beeramid(4, 4) == 1
assert beeramid(3, 4) == 0
assert beeramid(0, 4) == 0
assert beeramid(-1, 4) == 0
assert beeramid(10500, 2) == 24
"""


def beeramid(bonus: float, price: float) -> int:
    if bonus <= 0 or price <= 0:
        return 0
    num = bonus // price
    beer_sum = 0
    for i in range(0, int(num) + 1):
        beer_sum += i ** 2
        if beer_sum > num:
            i -= 1
            break
    return i


assert beeramid(9, 2) == 1
assert beeramid(10, 2) == 2
assert beeramid(11, 2) == 2
assert beeramid(21, 1.5) == 3
assert beeramid(454, 5) == 5
assert beeramid(455, 5) == 6
assert beeramid(4, 4) == 1
assert beeramid(3, 4) == 0
assert beeramid(0, 4) == 0
assert beeramid(-1, 4) == 0
assert beeramid(10500, 2) == 24
