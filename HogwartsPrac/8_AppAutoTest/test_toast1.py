from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestToast(object):
    def setup(self):
        caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.view.PopupMenu1",
            "automationName": "uiautomator2"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Search']").click()
        # print(self.driver.page_source)
        # 定位方法一：打印出 " Clicked popup menu item Search "
        # print(self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text)
        # 定位方法二：打印出 " Clicked popup menu item Search "
        print(self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text, 'Clicked popup')]").text)

