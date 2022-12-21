# 第一步：（以只读模式）打开文件
f = open('data.txt', 'r', encoding=' utf-8')
# 第二步:读取文件内容
print(f.read())
# 第三步:关闭文件
f.close()
