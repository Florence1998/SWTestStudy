import csv


def get_csv():
    with open("./demo.csv", "r", encoding="utf8") as file:  # "./demo.csv"：传入文件的名称。"r"：表示读取
        raw = csv.reader(file)  # 读取的是一个迭代器对象

        for line in raw:  # 遍历的时候，依次会得到第一行、第二行...的数据
            print(line)  # 每一行被获取时，都是一个列表对象。每一个逗号分隔的，就是列表的每一个元素


if __name__ == "__main__":
    get_csv()
