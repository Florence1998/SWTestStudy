# 实现一个计时器的装饰器，计算函数执行时间
# 三步走：1.定义一个外函数，外函数有一个形参，接受被装饰的函数对象
# 2.定义一个内函数，内函数内调用传入函数
# 3.定义外函数的返回值，外函数返回值固定格式为内函数对象
import datetime
import time


def timer(func):
    # 如果被装饰函数有参数，那么需要在内函数加形参，以及在函数调用的时候添加参数
    # 如果写死一个参数，但是无法确定被装饰函数的参数数量，会报错
    # 解决方案：把两个地方的参数都换成不定长参数
    def inner(*args, **kwargs):
        # 装饰器逻辑
        # 获取当前时间
        start_time = datetime.datetime.now()
        func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f"函数的执行时间：{end_time - start_time}")

    return inner


@timer
def hogwarts():
    print("霍格沃兹学社")
    time.sleep(2)


@timer
def hogwarts2(sleep_time):
    print("霍格沃兹学社2")
    time.sleep(sleep_time)


@timer
def hogwarts3(name, age, gender):
    print("霍格沃兹学社3")
    print(name)
    print(age)
    print(gender)


hogwarts()
hogwarts2(5)
hogwarts3("harry", 11, "男生")
