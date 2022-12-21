"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest

from web_practice.web_po.page.login_page import LoginPage

"""用例层，只关心业务"""


class TestAddMember:
    def setup_class(self):
        self.home = LoginPage().login()

    def setup(self):
        # mock 测试数据
        from faker import Faker
        fake = Faker('zh_CN')
        self.name = fake.name()
        self.phone_number = fake.phone_number()
        self.accid = fake.ssn()

    def teardown(self):
        pass

    def test_addmember(self):
        "登录->首页->添加成员->编辑/保存->验证"
        tips = self.home.click_add_member().fill_info(self.name, self.accid, self.phone_number).get_tips()
        assert "保存成功" == tips
