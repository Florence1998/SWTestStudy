import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestContact(object):
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

    def setup(self):
        # mock测试数据
        from faker import Faker
        fake = Faker('zh_CN')
        self.name = fake.name()
        self.accid = fake.ssn()
        self.phone_number = fake.phone_number()
        # 每次执行用例，都从home页面开始
        # 4.再次访问企业微信主页/刷新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def teardown_class(self):
        # 后置处理
        # 不要退出！！！防止互踢
        # self.driver.quit()
        pass

    def test_addmember(self):
        """通讯录页面：添加成员"""
        # ======1.点击通讯录
        self.driver.find_element(By.ID, "menu_contacts").click()
        # ======2.点击添加成员
        # 方法一（还是不行）：先等一个复杂元素出现，然后再去找【添加成员】按钮
        # search_box = (By.CSS_SELECTOR, ".qui_inputText")
        # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(search_box))
        # 点击添加成员按钮
        # self.driver.find_element(By.LINK_TEXT, "添加成员").click()
        # 方法二：显式等待，等输入框存在，再进行后续操作
        # 成功的点击添加成员 --->能够跳转到输入页面就算成功了！！！
        # 隐式等待 ： 去判断dom里是否存在这个元素
        # 显式等待： 真正地判断这些属性没有问题
        addmember_loc = (By.LINK_TEXT, "添加成员")

        def wait_for(x: WebDriver):
            try:
                # 显式等待会反复地执行这个方法
                # 1. 点击 【添加成员】
                x.find_element(*addmember_loc).click()
                # 2. 判断是否进入到一个页面，有输入框 username
                return x.find_element(By.ID, "username")
            except:
                return False
        # 两个条件退出显式等待的循环：1.找到元素，2.超时
        WebDriverWait(self.driver, 10).until(wait_for)
        # ======3.输入姓名、帐号、手机号
        self.driver.find_element(By.ID, "username").send_keys(self.name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(self.accid)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(self.phone_number)
        # ======4.点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        # ======5.验证添加成功
        result = self.driver.find_element(By.ID, "js_tips").text
        assert "保存成功" == result

    def test_addpart(self):
        """通讯录页面：添加部门"""
        part_name = "测试部门"
        # 1.点击通讯录
        self.driver.find_element(By.ID, "menu_contacts").click()
        # 2.点击【+】
        self.driver.find_element(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        # 3.点击 添加部门
        self.driver.find_element(By.LINK_TEXT, "添加部门").click()
        # 4.1 输入 部门名称
        self.driver.find_element(By.XPATH, "//*[@name='name']").send_keys(part_name)
        # 4.2 点击 所属部门
        self.driver.find_element(By.CSS_SELECTOR, ".js_parent_party_name").click()
        # 4.3 点击 格兰芬多
        self.driver.find_element(By.XPATH, "//div[@class='inputDlg_item']//a[text()='翟羽佳科技有限公司']").click()
        # 4.4 点击 确定
        self.driver.find_element(By.XPATH, "//a[text()='确定']").click()

        # 4、验证添加成功
        result = self.driver.find_element(By.ID, "js_tips").text
        # value = self.driver.find_element().get_attribute("data-usercardinit")
        assert "新建部门成功" == result