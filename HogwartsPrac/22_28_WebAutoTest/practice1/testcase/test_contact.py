import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAddMember(object):
    """添加成员"""

    def setup_class(self):
        # 前置动作
        # 准备资源文件，做初始化
        # 第一步：创建一个driver实例变量
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        """第二步：植入cookie完成登录"""
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

        # mock测试数据
        from faker import Faker
        fake = Faker('zh_CN')
        self.name = fake.name()
        self.accid = fake.ssn()
        self.phone_number = fake.phone_number()

    def teardown_class(self):
        # 后置处理
        # 不要退出！！！防止互踢
        self.driver.quit()

    def test_addmember(self):
        # name = "hogwarts001"
        # accid = "1234567"
        # phone_number = "13000000000"
        """功能：添加通讯录成员"""
        # 1.首页点击添加成员
        # 第一种写法---可以
        # self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        # 第二种写法---可以
        self.driver.find_elements(By.CSS_SELECTOR, ".index_service_cnt_item_title")[0].click()
        # 2.输入姓名、帐号、手机号
        self.driver.find_element(By.ID, "username").send_keys(self.name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(self.accid)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(self.phone_number)
        # 3.点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        # 4.验证添加成功
        result = self.driver.find_element(By.ID, "js_tips").text
        assert "保存成功" == result
