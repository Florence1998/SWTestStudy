from appium.webdriver import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class TestBrowser:
    def setup_class(self):
        # setup the web driver and launch the webview app.
        capabilities = {
            'platformName': 'Android',
            'browserName': 'chrome',
            # python appium client 2.x 需要追加这个参数
            'chromeOptions': {'w3c': False},
            'chromedriverExecutableDir': '/Users/seveniruby/projects/chromedriver/chromedrivers'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(10)

    def test_browser(self):
        self.driver.get("https://ceshiren.com")
        self.driver.find_element(AppiumBy.ID, 'search-button').click()
        self.driver.find_element(By.CSS_SELECTOR, '.search-query').send_keys('webview')
        self.driver.find_element(By.CSS_SELECTOR, 'button.search-cta').click()
        assert 'webview' in self.driver.find_element(By.CSS_SELECTOR, '.topic-title').text
