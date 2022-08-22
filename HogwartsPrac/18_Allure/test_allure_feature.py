import allure


@allure.feature("搜索模块")
class TestSearch(object):
    @allure.story("搜索成功")
    def test_case1(self):
        print("case1")

    @allure.story("搜索失败")
    def test_case2(self):
        print("case2")


@allure.feature("登录模块")
class TestLogin(object):
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：登录页面"):
            print("登录页面")
            allure.attach.file("D:/头像.jpg",
                               name="截图",
                               attachment_type=allure.attachment_type.JPG,
                               extension=".jpg")
        with allure.step("步骤3：输入用户信息"):
            print("输入用户名和密码")
            allure.attach("这是一段文本信息", name="文本展示")
        with allure.step("步骤4：进入成功页面"):
            allure.attach('<a href="http://news.baidu.com" target="_blank" class="mnav c-font-normal c-color-t">新闻</a>',
                          name="html展示",
                          attachment_type=allure.attachment_type.HTML)
            print("这是登录：测试用例，登录成功")


    @allure.story("登录成功")
    def test_login_success_a(self):
        print("这是登录：测试用例，登录成功")

    @allure.story("登录成功")
    def test_login_success_b(self):
        print("用户名缺失")

    @allure.story("登录失败")
    def test_login_failure(self):
        print("输入用户名")
        print("输入密码")
        print("点击登录")
        assert 1 == 1
        print("登录失败")

    @allure.story("登录失败")
    def test_login_failure_a(self):
        print("这是登录：测试用例，登录失败")
