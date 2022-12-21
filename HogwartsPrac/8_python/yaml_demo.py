import yaml
# 读取yaml文件中的内容，转化为python对象
with open("./my.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
print(data)
print(type(data))

