# 函数引用
def hogwarts():
    print("hogwarts")


hogwarts()  # 函数的调用
print(hogwarts)
print("==========")
harry = hogwarts  # 把函数对象赋值给一个变量，函数引用
print(harry)
peter = hogwarts
print(peter)
peter()
