from selenium import webdriver
from selenium.webdriver.common.by import By


def web_locate():
    # 首先需要实例化driver对象，Chrome()一定要加括号
    driver = webdriver.Chrome()
    # 打开一个网页
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 1.ID定位，第一个参数传递定位方式，第二个参数传递定位元素，调用这个方法的返回值为WebElement
    web_element = driver.find_element(By.ID, "locate_id")
    # web_element = driver.find_element_by_id("locate_id")：报错了，报错如下
    # AttributeError: 'WebDriver' object has no attribute 'find_element_by_id'
    # 老版本能执行成功，但“driver.find_element_by_id”方法书写时会有横线，说明这个方法在后续的版本更新中可能会直接被取消，建议不要使用
    # print(web_element)
    # 执行结果：<selenium.webdriver.remote.webelement.WebElement (session="19861d7b9193886634ba64faa53367fe", element="eb14e753-5fb2-4333-b986-16514deeeeb5")>
    # 2.Name定位
    # 如果报错no such element，代表元素定位可能出现错
    # driver.find_element(By.NAME, "locate11") # 错误示例
    # 如果没有报错，证明元素找到了
    # driver.find_element(By.NAME, "locate")
    # 3.CSS选择器定位
    # driver.find_element(By.CSS_SELECTOR, "#locate_id > a > span")
    # 4.xpath表达式定位
    # driver.find_element(By.XPATH, '//*[@id="locate_id"]/a/span')  # 里面是“”，外面就要用‘’
    # 5.通过链接文本的方式（1）元素一定是a标签 （2）输入的元素为标签内的文本
    driver.find_element(By.LINK_TEXT, "元素定位").click()


if __name__ == "__main__":
    web_locate()
