"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 工具类
# 获取 add.yml 文件中的数据
import os

import yaml


# 获取yaml 路径
def get_yaml_path():
    # __file__ == util.py
    path = os.path.abspath(__file__)
    demopath = os.path.dirname(path)
    addpath = "datas/add.yml"
    finalpath = os.path.join(demopath, "..", addpath)
    return finalpath


# 获取yaml 数据
def get_adddata(name, level):
    # 绝对路径
    # os.path.abspath()
    # __file__
    with open(get_yaml_path(), encoding="utf-8") as f:
        # safe_load() 将 yaml 格式转成 python 对象
        result = yaml.safe_load(f)
        # ids = yaml.safe_load(f).get(name).get(level).get('ids')
    # P0 测试数据
    data = result.get(name).get(level).get('data')
    # P0 测试用例别名
    ids = result.get(name).get(level).get('ids')
    print(f"测试数据：{data}, 测试用例别名：{ids}")
    return data, ids
