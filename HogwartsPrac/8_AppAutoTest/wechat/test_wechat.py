from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWechat:
    def setup_class(self):
        capabilities = {
            'platformName': 'android',
            # 为了不清理微信数据
            'noReset': True,
            'appPackage': 'com.tencent.mm',
            'appActivity': 'com.tencent.mm.ui.LauncherUI',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'showChromedriverLog': True,
            # appium bug 切换context时会把xweb当成webview，需要借助adb xweb mock技术修复
            'adbPort': 5038,
            'chromedriverExecutable': '/Users/seveniruby/projects/chromedriver/chromedrivers/chromedriver_86.0.4240',
            # appium bug 会自动覆盖自己配置的mapping file，太智能了反而导致了bug
            # 'chromedriverChromeMappingFile': '/Users/seveniruby/PycharmProjects/AppiumDemo/mapping.json',
            # 'chromedriverExecutableDir': '/Users/seveniruby/projects/chromedriver/chromedrivers'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(10)

    def test_wechat(self):
        self.driver.find_element(By.CSS_SELECTOR, '*[description="搜索"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'android.widget.EditText').send_keys("美团外卖")
        self.driver.find_element(By.XPATH, '//*[contains(@text, "外卖美食")]').click()

        print(self.driver.contexts)
        wait = WebDriverWait(self.driver, 5)
        # 个别app webview组件加载慢的时候不一定会及时出现webview上下文，需要加显式等待
        wait.until(lambda driver: filter(lambda c: "appbrand" in c, self.driver.contexts))
        print(self.driver.contexts)

        # 进入第一个打开的小程序
        self.driver.switch_to.context("WEBVIEW_com.tencent.mm:appbrand0")
        self.driver.implicitly_wait(10)
        self.switch_to_visible_window("/index/index.html")

        search_button = self.driver.find_element(By.CSS_SELECTOR, '.search-index--ellipsis')
        wait.until(expected_conditions.element_to_be_clickable(search_button))
        search_button.click()

        self.switch_to_visible_window("/search/search.html")
        self.driver.find_element(By.CSS_SELECTOR, '#search_input').click()

        print("输入")
        # 只能用这个办法输入
        self.driver.switch_to.context("NATIVE_APP")
        self.driver.execute_script("mobile: type", {"text": "啤酒炸鸡"})
        self.driver.switch_to.context("WEBVIEW_com.tencent.mm:appbrand0")

        print("点击搜索按钮")
        self.driver.find_element(By.CSS_SELECTOR, '#search_button').click()

        print("后退")
        self.driver.switch_to.context("NATIVE_APP")
        self.driver.back()
        self.driver.switch_to.context("WEBVIEW_com.tencent.mm:appbrand0")

        print("断言")
        self.switch_to_visible_window("/search/search.html")
        assert "啤酒炸鸡" in self.driver.find_element(By.CSS_SELECTOR, '[data-history=true]').text

    def switch_to_visible_window(self, pattern=":VISIBLE"):
        signal = False
        while not signal:
            for window in self.driver.window_handles:
                print(window)
                self.driver.switch_to.window(window)
                print(self.driver.current_url)
                print(self.driver.title)
                # 进入可视化的页面
                if pattern in self.driver.title:
                    print(pattern)
                    signal = True
                    break
