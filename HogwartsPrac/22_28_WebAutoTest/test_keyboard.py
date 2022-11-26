import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class TestKeyboard(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_shift(self):
        """
        1.访问 https://ceshiren.com/ 官方网站
        2.点击搜索按钮
        3.输入搜索的内容，输入的同时按着shift键
        :return:
        """
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.ID, "search-button").click()
        # self.driver.find_element(By.ID, "search-term").send_keys("appnium")
        # 目标元素即为输入框
        ele = self.driver.find_element(By.ID, "search-term")
        # 1.key_down代表按下某个键位
        # 2.输入内容
        # 3.执行以上操作
        ActionChains(self.driver)\
            .key_down(Keys.SHIFT, ele)\
            .send_keys("selenium")\
            .perform()
        time.sleep(3)

    def test_enter_by_send_keys(self):
        self.driver.get("https://sogou.com/")
        self.driver.find_element(By.ID, "query").send_keys("霍格沃兹测试开发")
        time.sleep(3)
        # 第一种回车方式
        # self.driver.find_element(By.ID, "query").send_keys(Keys.ENTER)
        # 第二种回车方式
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        time.sleep(3)

    def test_copy_and_paste(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.ID, "search-button").click()
        # 目标元素即为输入框
        ele = self.driver.find_element(By.ID, "search-term")
        cmd_ctrl = Keys.COMMAND if sys.platform == "darwin" else Keys.CONTROL
        ActionChains(self.driver)\
            .key_down(Keys.SHIFT, ele)\
            .send_keys("selenium!")\
            .send_keys(Keys.ARROW_LEFT)\
            .key_down(cmd_ctrl).send_keys("xvv").key_up(cmd_ctrl)\
            .perform()
        time.sleep(3)

