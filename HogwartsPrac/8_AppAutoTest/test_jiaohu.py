from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestSearch(object):
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator-5554"
        caps["uuid"] = "emulator-5554"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["unicodeKeyBoard"] = "true"
        caps["resetKeyBoard"] = "true"
        caps["avd"] = "Pixel_3a_API_33_x86_64"  # 自动启动emulator模拟器
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(25)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        self.driver.start_recording_screen()
        self.driver.make_gsm_call('15195383763', GsmCallActions.CALL)
        self.driver.send_sms('15195383763', "hi，我是翟羽佳的短信")
        self.driver.get_screenshot_as_file('./photos/img.png')
        # self.driver.set_network_connection(1)  # 设置飞行模式
        # sleep(3)
        # self.driver.get_screenshot_as_file('./photos/img1.png')
        # self.driver.set_network_connection(4)  # 设置移动数据模式
        # sleep(3)
        self.driver.stop_recording_screen()


