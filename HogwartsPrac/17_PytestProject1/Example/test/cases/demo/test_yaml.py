"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# yaml 保存数据
# pip install pyyaml
import os

import yaml


# def test_load():
#     # with 执行完代码块会自动关闭文件
#     with open("../../datas/demo.yml") as f:
#         # safe_load() 将 yaml 格式转成 python 对象
#         result = yaml.safe_load(f)
#     print(result)
#
# def test_load_adddata():
#     # with 执行完代码块会自动关闭文件
#     with open("../../datas/add.yml") as f:
#         # safe_load() 将 yaml 格式转成 python 对象
#         result = yaml.safe_load(f)
#     # P0 测试数据
#     data = result.get("add").get('P0').get('data')
#     # P0 测试用例别名
#     ids = result.get("add").get('P0').get('ids')
#
#     print(f"测试数据：{data}, 测试用例别名：{ids}")
#     return data,ids
#
# def test_load_adddata1(name, level):
#     """
#     :param name:用例范围
#     :param level:级别
#     :return:
#     """
#     # with 执行完代码块会自动关闭文件
#     with open("../../datas/add.yml") as f:
#         # safe_load() 将 yaml 格式转成 python 对象
#         result = yaml.safe_load(f)
#     # P0 测试数据
#     data = result.get(name).get(level).get('data')
#     # P0 测试用例别名
#     ids = result.get(name).get(level).get('ids')
#     print(f"测试数据：{data}, 测试用例别名：{ids}")
#     return data,ids
#
# def load_adddata2(name, level):
#     """
#     :param name:用例范围
#     :param level:级别
#     :return:
#     """
#     # with 执行完代码块会自动关闭文件
#     with open("../../datas/add.yml",encoding="utf-8") as f:
#         # safe_load() 将 yaml 格式转成 python 对象
#         result = yaml.safe_load(f)
#         # ids = yaml.safe_load(f).get(name).get(level).get('ids')
#     # P0 测试数据
#     data = result.get(name).get(level).get('data')
#     # P0 测试用例别名
#     ids = result.get(name).get(level).get('ids')
#     print(f"测试数据：{data}, 测试用例别名：{ids}")
#     return data,ids


def test_dump():
    # 将python 对象转成 yaml 格式对象
    data = {"add": [[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02], [10, 2, 12]]}
    with open("data.yml", mode='w', encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True)


# def test_getdata_param():
#     load_adddata2("add", "P0")

def test_path():
    # 绝对路径,路径+文件名
    # __file__  python内置变量，代表 当前模块
    # os.path.abspath  获取绝对路径 （路径+文件名）
    # os.path.dirname 获取路径
    # os.path.join 连接路径

    path = os.path.abspath(__file__)
    print(path)
    print(os.path.dirname(path))
    demopath = os.path.dirname(path)
    addpath = "datas/add.yml"
    add_finalpath = os.path.join(demopath, "../..", addpath)
    with open(add_finalpath) as f:
        result = yaml.safe_load(f)
        print(result)
