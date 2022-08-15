try:
    a = int(input("输入被除数："))
    b = int(input("输入除数："))
    c = a / b
    print("您输入的两个数相除的结果是：", c)
except ValueError:
    print("程序发生了数字格式异常,输入非数字")
except:
    print("未知异常")
print("程序继续运行")
