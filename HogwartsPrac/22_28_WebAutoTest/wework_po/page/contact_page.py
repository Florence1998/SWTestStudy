"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from web_practice.web_po.page.base import Base
from web_practice.web_po.util.log_util import logger


class ContactPage(Base):
    _TEXT_TIPS = By.ID, "js_tips"

    def get_tips(self):
        """获取添加成功提示"""
        logger.info("获取添加成功提示")
        result = self.do_find(self._TEXT_TIPS).text
        return result
