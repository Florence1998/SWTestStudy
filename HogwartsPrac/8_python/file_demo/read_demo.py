with open('data.txt ', 'r', encoding='utf-8') as f:
    print(f.read())
print(f.closed)  # 查看关闭状态，如果关闭掉了，会返回True
