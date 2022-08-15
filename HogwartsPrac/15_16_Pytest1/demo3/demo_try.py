try:
    a = int(input("输入被除数："))
    b = int(input("输入除数："))
    c = a / b
    print("您输入的两个数相除的结果是：", c)
except ValueError:  # 除数为0，格式为0，都会被异常捕获掉，然后去打印相关的一些信息
    print("程序发生了数字格式异常，输入为非数字")
except ZeroDivisionError:
    print("程序发生了算数异常，除数为0")
except Exception:
    print("未知异常")
print("程序继续运行")
