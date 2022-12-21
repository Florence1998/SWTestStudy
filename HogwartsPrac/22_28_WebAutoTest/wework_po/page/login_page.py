"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import yaml

from web_practice.web_po.page.base import Base
from web_practice.web_po.page.home_page import HomePage
from web_practice.web_po.util.log_util import logger

"""登录页面"""


class LoginPage(Base):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame"

    def login(self):
        """登录"""
        logger.info("cookie登录")
        """第二步：植入cookie完成登录"""
        # 1、访问企业微信主页
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 2、获取本地的cookies
        with open("../datas/cookies.yaml") as f:
            # yaml 格式 转成python 对象
            cookies = yaml.safe_load(f)

        # 3、植入cookies
        for cookie in cookies:
            # cookie 就是一个字典
            self.driver.add_cookie(cookie)
        # 4、再次访问企业微信主页/ 刷新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        return HomePage(self.driver)
