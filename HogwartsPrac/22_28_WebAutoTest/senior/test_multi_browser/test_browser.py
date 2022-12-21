from selenium import webdriver

from senior.test_multi_browser.conftest import web_env


class TestBrowser(object):
    def setup_class(self):
        self.browser = web_env.get("browser")

    def test_ceshiren(self):
        print(f"获取到的浏览器信息为{self.browser}")
        if self.browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.quit()
