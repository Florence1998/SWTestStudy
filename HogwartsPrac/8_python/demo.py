# 需求：a == 1时，flag = True
import logging

logging.basicConfig(level=logging.INFO)
a = 1
b = 2
if a == 1:
    flag = False
    # print(f"a == 1：flag = {flag}")  # 对应位置使用`print`打印日志信息
    logging.info(f"a == 1：flag = {flag}")  # 对应位置使用`logging`打印日志信息
else:
    flag = True
    # print(f"else：flag = {flag}")
print(flag)
