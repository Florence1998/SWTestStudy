from selenium import webdriver
import time


# 打开浏览器
def open_browser():
    driver = webdriver.Chrome()
    # 调用get方法是需要传递浏览器的url
    driver.get("https://ceshiren.com/")
    time.sleep(2)
    # 刷新浏览器
    driver.refresh()
    # 通过get跳转到baidu
    driver.get("https://www.baidu.com/")
    # 退回上一步，返回百度之前的页面，也就是测试人页面
    driver.back()
    # 最大化浏览器
    driver.maximize_window()
    time.sleep(2)
    # 最小化浏览器
    driver.minimize_window()
    time.sleep(2)


# 刷新浏览器

# 退回操作

# 最大化

# 最小化
if __name__ == '__main__':
    # 1.打开浏览器1
    # 2.刷新浏览器
    # 3.打开浏览器2
    # 4.回退浏览器
    # 5.最大化浏览器
    # 6.最小化浏览器
    open_browser()
