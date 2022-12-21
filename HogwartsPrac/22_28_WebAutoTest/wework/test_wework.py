import time

import yaml
from selenium import webdriver


class TestCookieLogin(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()

    def test_get_cookies(self):
        # 1.访问企业微信主页/登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 2.等待20s，人工扫码操作
        time.sleep(20)
        # 3.等成功登录之后，再去获取cookie信息
        cookie = self.driver.get_cookies()
        # 将cookie存入一个可吃就存储的地方，文件
        # 打开文件的时候添加写入权限
        with open("cookie.yaml", "w") as f:
            # 第一个参数是要写入的数据
            yaml.safe_dump(cookie, f)  # 需要setting安装PyYAML第三方库，并且导包

    def test_add_cookie(self):
        # 1.访问企业微信主页/登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 2.定义cookie，先手动粘贴，随后优化
        cookie = yaml.safe_load(open("cookie.yaml"))
        # 3.植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(3)
        # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")