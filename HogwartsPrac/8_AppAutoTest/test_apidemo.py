from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestApiDemo(object):
    def setup(self):
        caps = {}
        caps["deviceName"] = "127.0.0.1:7555"
        caps["platformName"] = "Android"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def test_id(self):
        """通过id进行元素定位"""
        """Android：resource-id"""
        elements = self.driver.find_elements(AppiumBy.ID, "android:id/text1")
        elements[3].click()

    def test_accessibility_id(self):
        """通过accessibility id进行元素定位"""
        """Android：content-desc"""
        element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Content")
        element.click()

    def test_xpath(self):
        """通过xpath进行元素定位"""
        """//*[@属性名='属性值']"""
        element = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Content']")
        element.click()

    def test_xpath_more(self):
        """通过xpath多条件进行元素定位"""
        """//*[@属性名='属性值' and @属性名='属性值' ]"""
        element = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/text1' and @text='Content']")
        element.click()

    def test_android_uiautomator(self):
        """通过android uiautomator单属性进行元素定位"""
        """'new UiSelector().属性名("<属性值>")'"""
        element = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                           'new UiSelector().resourceId("android:id/text1")')
        element.click()
