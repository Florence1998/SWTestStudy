from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class TestAction(object):
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appium:deviceName"] = "127.0.0.1:7555"
        caps["appium:appPackage"] = "cn.kmob.screenfingermovelock"
        caps["appium:appActivity"] = "com.samsung.ui.FlashActivity"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_action(self):
        # 设置手势
        el1 = self.driver.find_element(by=AppiumBy.ID, value="cn.kmob.screenfingermovelock:id/setPatternLayout")
        el1.click()
        # 定义ActionChains实例
        actions = ActionChains(self.driver)
        # 定义输入源
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        # 定义动作 按下→滑动→抬起
        actions.w3c_actions.pointer_action.move_to_location(118, 176)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(335, 176)
        actions.w3c_actions.pointer_action.pause(0.5)  # 暂停0.5秒
        actions.w3c_actions.pointer_action.move_to_location(614, 161)
        actions.w3c_actions.pointer_action.pause(0.5)
        actions.w3c_actions.pointer_action.move_to_location(598, 423)
        actions.w3c_actions.pointer_action.pause(0.5)
        # 最后的点
        actions.w3c_actions.pointer_action.move_to_location(598, 659)
        # 释放 抬起的动作
        actions.w3c_actions.pointer_action.release()
        # 执行动作
        actions.perform()
