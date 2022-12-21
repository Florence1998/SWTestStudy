"""登录"""
import time

import yaml
from selenium import webdriver


# 账号会互顶！！！！
class TestCookieLogin(object):
    def setup_class(self):
        # 前置动作
        # 准备资源文件，做初始化
        # 创建一个driver实例变量
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_class(self):
        # 后置处理
        # self.driver.quit()
        pass

    def test_get_cookie(self):
        """获取cookie"""
        # 1.访问企业微信
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 2.扫码，手动登录
        time.sleep(20)
        # 3.登录后，获取cookie
        cookies = self.driver.get_cookies()
        # 4.保存cookie
        with open("../datas/cookies.yaml", "w") as f:
            # python对象转成yaml格式
            yaml.safe_dump(data=cookies, stream=f)

    def test_add_cookie(self):
        """植入cookie"""
        # 1.访问企业微信主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 2.获取本地的cookies
        with open("../datas/cookies.yaml", "r", encoding="utf-8") as f:
            cookies = yaml.safe_load(f)
        # 3.植入cookies
        for cookie in cookies:
            # cookie就是一个字典
            self.driver.add_cookie(cookie)
        # 4.再次访问企业微信主页/刷新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(3)
