import logging
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestSearch(object):
    def setup(self):
        # 创建一个字典，desire capability
        caps = {}
        caps["platformName"] = "Android"
        # Android 包名和页面名，获取命令：
        # Mac/Linux: adb logcat ActivityManager:I | grep “cmp"
        # Windows: aapt dump badging wework.apk  | findstr “cmp”
        # com.xueqiu.android/.view.WelcomeActivityAlias
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["deviceName"] = "127.0.0.1:7555"  # 设备名，一个标识，取啥名都行
        caps["noReset"] = "true"  # 保留登录信息（缓存），不写的话执行时会清缓存，清掉登录信息
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)  # 隐式等待，是一种全局等待，对第三方软件，启动加载比较慢的比较有用

    def teardown(self):
        # 关闭应用
        self.driver.quit()

    def test_search(self):
        """
        1.判断搜索框是否可用,并查看搜索框 name 属性值，并获取搜索框坐标，以及它的宽高
        2.点击搜索框
        3.向搜索框输入:alibaba
        4.判断【阿里巴巴】是否可见
            如果可见，打印“搜索成功”
            如果不可见，打印“搜索失败”
        """
        search_key = "alibaba"
        # 1.判断搜索框是否可用,并查看搜索框 name 属性值，并获取搜索框坐标，以及它的宽高
        searchbox_ele = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/tv_search")
        # 先判断一下搜索框是否可用
        if searchbox_ele.is_enabled():
            searchbox_text = searchbox_ele.get_attribute("text")
            searchbox_location = searchbox_ele.location
            searchbox_size = searchbox_ele.size
            print(f"首页搜索框的text属性值为：{searchbox_text}")
            print(f"首页搜索框的坐标为：{searchbox_location}")
            print(f"首页搜索框的宽高为：{searchbox_size}")
            # 2.点击搜索框
            searchbox_ele.click()
            # 3.向搜索框输入:alibaba
            self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(search_key)
            # 4.判断【阿里巴巴】是否可见:如果可见，打印“搜索成功”;如果不可见，打印“搜索失败”
            alibaba_ele = self.driver.find_element(AppiumBy.XPATH, "//*[@text='阿里巴巴']")
            result = alibaba_ele.is_displayed()
            if result == "True":
                print("搜索成功")
            else:
                print("搜索失败")
            assert result == True
        else:
            print("搜索框不可用")
            assert False

    def test_get_current(self):
        search_key = "alibaba"
        # 1.点击搜索框
        self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/tv_search").click()
        # 2.向搜索框输入:alibaba
        self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(search_key)
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='阿里巴巴']").click()
        current_price = self.driver.find_element(AppiumBy.XPATH,
                                                 "//*[@text='BABA']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"当前阿里巴巴（BABA）对应的股票价格是：{current_price}")
        assert float(current_price) < 200

    def test_myinfo(self):
        """
        1.点击我的，进入到个人信息页面
        2.点击登录，进入到登录页面
        3.输入用户名，输入密码
        4.点击登录
        :return:
        """
        # self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().text("我的").resourceId("com.xueqiu.android:id/tab_name").className("android.widget.TextView")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("帐号密码登录")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys(
            "12345")
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys(
            "12345zyj")
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        time.sleep(3)

    def test_search1(self):
        """
        通过css改写
        1.判断搜索框是否可用
        2.点击搜索框
        3.向搜索框输入:alibaba
        4.判断【阿里巴巴】是否可见
            如果可见，打印“搜索成功”
            如果不可见，打印“搜索失败”
        """
        search_key = "alibaba"
        # 1.判断搜索框是否可用,并查看搜索框 name 属性值，并获取搜索框坐标，以及它的宽高
        # searchbox_ele = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/tv_search")
        searchbox_ele = self.driver.find_element(AppiumBy.CSS_SELECTOR, "#com\.xueqiu\.android\:id\/tv_search")
        # 先判断一下搜索框是否可用
        if searchbox_ele.is_enabled():
            # 2.点击搜索框
            searchbox_ele.click()
            # 3.向搜索框输入:alibaba
            # self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(search_key)
            self.driver.find_element(AppiumBy.CSS_SELECTOR, "#com\.xueqiu\.android\:id\/search_input_text").send_keys(
                search_key)
            # 4.判断【阿里巴巴】是否可见:如果可见，打印“搜索成功”;如果不可见，打印“搜索失败”
            # alibaba_ele = self.driver.find_element(AppiumBy.XPATH, "//*[@text='阿里巴巴']")
            alibaba_ele = self.driver.find_element(AppiumBy.CSS_SELECTOR, "*[text='阿里巴巴']")
            result = alibaba_ele.is_displayed()
            if result == "True":
                print("搜索成功")
            else:
                print("搜索失败")
            assert result == True
        else:
            print("搜索框不可用")
            assert False

    def test_search3(self):
        """使用 xpath 定位"""
        logging.info("搜索用例")
        element = self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/tv_search']")
        search_enabled = element.is_enabled()
        logging.info(f"搜索框的文本：{element.text}，搜索框的坐标：{element.location}，搜索框的size：{element.size}")
        if search_enabled:
            logging.info("点击搜索框")
            element.click()
            logging.info(f"向搜索框中输入内容：alibaba")
            self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("alibaba")
            alibaba_element = self.driver.find_element(AppiumBy.XPATH, "//*[@text='阿里巴巴']")

            # alibaba_element.is_displayed()
            displayed = alibaba_element.get_attribute("displayed")
            logging.info("搜索结果是否处于显示状态："+displayed)
            logging.info("搜索结果页的页面源码为：" + self.driver.page_source)
            self.driver.save_screenshot("./image/search_result.png")
            assert displayed == "true"
