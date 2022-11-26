"""
皮特喜欢烤一些蛋糕。他有一些食谱和配料。可惜他数学不好。你能帮他找出，考虑到他的食谱，他能烤多少蛋糕？

编写一个函数cakes() ，它接受食谱（对象）和可用成分（也是一个对象）并返回皮特可以烘烤的最大蛋糕数量（整数）。为简单起见，数量没有单位（例如，1 磅面粉或 200 克糖只是 1 或 200）。对象中不存在的成分可以视为 0。

例子：

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
题目难度：一般
题目来源： Pete, the baker | Codewars 6

def cakes(recipe, available):
    # your code
    return
recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
assert cakes(recipe, available) == 2

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
assert cakes(recipe, available) == 0
"""


def cakes(recipe, available):
    need_foods = recipe.keys()
    have_foods = available.keys()
    my_list = []
    for need_food in need_foods:
        if need_food not in have_foods:  # 如果菜谱食材，在实际食材中找不到，返回0
            my_list.append(0)
            break
        for have_food in have_foods:
            if need_food == have_food:  # 如果菜谱食材，在实际食材中能找到，找到相同食材
                my_list.append(available[have_food] // recipe[need_food])  # 通过整除，判断能做几份
    my_list.sort()  # 找到份数的最小值，即最终能做的份数
    return my_list[0]


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
assert cakes(recipe, available) == 2

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
assert cakes(recipe, available) == 0
