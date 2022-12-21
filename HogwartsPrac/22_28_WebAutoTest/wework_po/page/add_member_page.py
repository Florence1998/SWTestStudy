"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from selenium.webdriver.common.by import By

from web_practice.web_po.page.base import Base
from web_practice.web_po.page.contact_page import ContactPage
from web_practice.web_po.util.log_util import logger


class AddMemberPage(Base):
    _INPUT_USERNAME = (By.ID, "username")
    _INPUT_ACCIT = By.ID, "memberAdd_acctid"
    _INPUT_PHONENUMBER = (By.ID, "memberAdd_phone")
    _BTN_SAVE = (By.CSS_SELECTOR, ".js_btn_save")

    def fill_info(self, name, accid, phone_number):
        logger.info("输入内容")
        # input username,phonenumber,accid
        # 点击保存
        self.do_send_keys(name, self._INPUT_USERNAME)
        self.do_send_keys(accid, self._INPUT_ACCIT)
        self.do_send_keys(phone_number, self._INPUT_PHONENUMBER)

        # 3、点击保存
        self.do_find(self._BTN_SAVE).click()
        return ContactPage(self.driver)
