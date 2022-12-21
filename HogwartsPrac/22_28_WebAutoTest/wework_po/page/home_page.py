"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from web_practice.web_po.page.add_member_page import AddMemberPage
from web_practice.web_po.page.base import Base
from web_practice.web_po.util.log_util import logger


class HomePage(Base):
    _BTN_ADDMEMBER = (By.CSS_SELECTOR, ".index_service_cnt_item_title")

    def click_add_member(self):
        # 点击【添加成员】
        logger.info("点击【添加成员】")
        self.do_find(self._BTN_ADDMEMBER).click()
        return AddMemberPage(self.driver)
