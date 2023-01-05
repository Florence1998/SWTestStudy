# 导入 pip install appium-python-client
from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestAppDemo(object):
    def setup(self):
        # 创建一个字典，desire capability
        caps = {}
        caps["platformName"] = "Android"
        # Android 包名和页面名，获取命令：
        # Mac/Linux: adb logcat ActivityManager:I | grep “cmp"
        # Windows: aapt dump badging wework.apk  | findstr launchable-activity
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["deviceName"] = "127.0.0.1:7555"  # 设备名，一个标识，取啥名都行
        caps["noReset"] = "true"  # 保留登录信息（缓存），不写的话执行时会清缓存，清掉登录信息
        # caps["ensureWebviewsHavePages"] = True  # 老师演示的时候直接删了，也没说啥
        # 创建driver，与appium server建立连接，返回一个session
        # driver变成self.driver，由局部变量变成实例变量，就可以在其他的方法中引用这个实例变量了
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)  # 对第三方软件，启动加载比较慢的比较有用

    def teardown(self):
        # 回收session
        self.driver.quit()

    def test_input(self):
        # el1：点击 OS ，进入下一个页面
        # el1 = self.driver.find_element_by_accessibility_id("OS")
        el1 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OS")
        el1.click()  # 调用点击方法
        # el2：点击 Morse Code
        # el2 = self.driver.find_element_by_accessibility_id("Morse Code")
        el2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Morse Code")
        el2.click()
        # el3 = self.driver.find_element_by_id("io.appium.android.apis:id/text")
        el3 = self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/text")
        # 清除原有的内容
        el3.clear()
        # 调用sendkeys方法，输入ceshiren.com
        el3.send_keys("ceshiren.com")
        el3.clear()
        # 手动制造关闭应用
        sleep(5)
        # 启动应用，热启动，会进入到app的首页 (没有杀掉进程，直接打开进入首页)
        self.driver.launch_app()
        # 返回
        self.driver.back()
        # 返回
        self.driver.back()
        result = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Accessibility").text
        # 断言
        assert result == "Accessibility"

    def test_seeking(self):
        """
        打开demo.apk
        1.点击Animation进入下个页面
        2.点击Seeking进入下个页面
        3.查看【RUN】按钮是否显示/是否可点击
        4.查看【滑动条】是否显示/是否可用/是否可点击
        5.获取【滑动条】长度
        6.点击【滑动条】中心位置
        :return:
        """
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Animation").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Seeking").click()
        # 3.查看【RUN】按钮是否显示/是否可点击
        run_element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Run")
        run_is_displayed = run_element.is_displayed()
        run_is_clicked = run_element.get_attribute("clickable")
        print(f"【run】按钮是否可见：{run_is_displayed}，是否可点击：{run_is_clicked}")
        # 4.查看【滑动条】是否显示/是否可用/是否可点击
        seekbar_element = self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/seekBar")
        seekbar_displayed = seekbar_element.is_displayed()
        seekbar_enabled = seekbar_element.is_enabled()
        seekbar_clicked = seekbar_element.get_attribute("clickable")
        print(f"seekbar滑动条是否可见：{seekbar_displayed}，是否可用：{seekbar_enabled}，是否可点击：{seekbar_clicked}")
        # 5.获取【滑动条】长度
        seekbar_size = seekbar_element.size
        seekbar_height = seekbar_size.get("height")
        seekbar_width = seekbar_size.get("width")
        print(f"seekbar滑动条的尺寸为：{seekbar_size}，高度为：{seekbar_height}，长度为：{seekbar_width}")
        # 6.点击【滑动条】中心位置
        seekbar_location = seekbar_element.location
        seekbar_x = seekbar_location.get("x")
        seekbar_y = seekbar_location.get("y")
        seekbar_centrey = seekbar_y
        seekbar_centrex = seekbar_x + seekbar_width/2
        self.driver.tap([(seekbar_centrex, seekbar_centrey)])
        sleep(3)


