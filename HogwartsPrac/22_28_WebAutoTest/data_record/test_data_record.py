from selenium import webdriver
from selenium.webdriver.common.by import By

from data_record.log_utils import logger


class TestDateRecord(object):
    def setup_class(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        # 关闭浏览器进程
        self.driver.quit()

    def test_log_data_record(self):
        # 进入搜狗首页
        self.driver.get("https://sogou.com/")
        # 输入霍格沃兹测试开发，进行搜索操作
        search_content = "霍格沃兹测试开发"
        self.driver.find_element(By.CSS_SELECTOR, "#query").send_keys(search_content)
        # debug记录步骤信息
        logger.debug(f"搜索的信息为{search_content}")
        self.driver.find_element(By.CSS_SELECTOR, "#stb").click()
        search_res = self.driver.find_element(By.CSS_SELECTOR, "em").text
        # info记录关键信息，比如断言等
        logger.info(f"实际结果为{search_res}，预期结果为{search_content}")
        assert search_res == search_content

    def test_screen_shot_data_record(self):
        # 步骤1：进入搜狗首页
        self.driver.get("https://sogou.com/")
        # 步骤2：输入霍格沃兹测试开发，进行搜索操作
        search_content = "霍格沃兹测试开发"
        self.driver.find_element(By.CSS_SELECTOR, "#query").send_keys(search_content)
        # debug记录步骤信息
        logger.debug(f"搜索的信息为{search_content}")
        self.driver.find_element(By.CSS_SELECTOR, "#stb").click()
        search_res = self.driver.find_element(By.CSS_SELECTOR, "em").text
        # 步骤3：判断搜索结果是否与搜索词一致
        # info记录关键信息，比如断言等
        logger.info(f"实际结果为{search_res}，预期结果为{search_content}")
        # 截图记录，双重保障
        self.driver.save_screenshot("search_res.png")
        assert search_res == search_content

    def test_page_source_data_record(self):
        # 现象：产生了NoSuchElementException错误
        # 解决方案：在报错的代码行之前打印page_source，确认定位的元素没有问题
        # 步骤1：进入搜狗首页
        self.driver.get("https://sogou.com/")
        # 步骤2：输入霍格沃兹测试开发，进行搜索操作
        search_content = "霍格沃兹测试开发"
        with open("record.html", "w", encoding="u8") as f:
            f.write(self.driver.page_source)
        self.driver.find_element(By.CSS_SELECTOR, "#query1").send_keys(search_content)
