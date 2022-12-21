import time

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from litemall.utils.log_utils import logger


# ===问题1：用例产生了脏数据
# 解决方案：清理对应的脏数据。清理的方式可以通过接口也可以通过ui的方式（老师把页面的删除按钮去了，只能通过接口的方式）


class TestLitemall(object):
    # 前置动作
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        # 步骤1：打开页面
        self.driver.get("https://litemall.hogwarts.ceshiren.com/")
        # 窗口最大化
        self.driver.maximize_window()
        # 问题：输入框内有默认值，此时send_keys不会清空只会追加
        # 解决方案：在输入信息之前，先对输入框完成清空
        # 步骤2：输入用户名密码登录
        self.driver.find_element(By.CSS_SELECTOR, "[name='username']").clear()
        self.driver.find_element(By.CSS_SELECTOR, "[name='username']").send_keys("hogwarts")
        self.driver.find_element(By.CSS_SELECTOR, "[name='password']").clear()
        self.driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("test12345")
        # 点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()

    # 后置动作
    def teardown_class(self):
        self.driver.quit()

    def get_screen(self):
        timestamp = int(time.time())
        # 注意!!一定要提前创建好images路径
        image_path = f"./images/image_{timestamp}.PNG"
        # 截图
        self.driver.save_screenshot(image_path)
        # 将截图放到报告的数据中
        allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)

    # 添加商品类目
    def test_add_type(self):
        # 步骤1：点击商场管理-商品类目，进入商品类目页面
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()
        # 步骤2：点击“添加”按钮，输入类目名称，点击确定
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("新增商品测试")  # 一定要定位到input标签!!!

        # =================使用显示等待优化
        # ele = WebDriverWait(self.driver, 10).until(
        #     expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".dialog-footer .el-button--primary")))
        # ele.click()
        # =================显示等待优化方案2：自定义显式等待
        def click_exception(by, element, max_attempts=5):
            def _inner(driver):  # 定义了一个内函数
                # 多次点击按钮
                actual_attempts = 0  # 实际点击次数
                while actual_attempts <= 5:
                    # 进行点击操作
                    actual_attempts += 1  # 每次循环，实际点击次数加1
                    try:
                        # 如果点击过程报错，则直接执行except逻辑，并且继续循环
                        # 如果没有报错，则直接return，循环结束
                        self.driver.find_element(by, element).click()
                        return True
                    except Exception:
                        logger.debug("点击的时候出现了一次异常")
                # 当实际点击次数大于最大点击次数时，结束循环并抛出异常
                raise Exception("超出了最大点击次数")

            # return _inner() 错误写法
            return _inner

        WebDriverWait(self.driver, 10).until(click_exception(By.CSS_SELECTOR, ".dialog-footer .el-button--primary"))
        # find_elements如果没有找到会返回空列表，find_element如果没找到会直接报错
        # 如果没找到，程序也不应该报错
        res = self.driver.find_elements(By.XPATH, "//*[text()='新增商品测试']")
        # 数据的清理一定要放到断言之后完成，要不然可能会影响断言结果
        # 此处接口或ui的方式清理脏数据
        # 断言产品新增后是否成功找到，如果找到，证明新增成功，如果没找到则新增失败
        # 判断查找的产品是否为空列表，如果为空列表证明没找到，反之代表元素找到，用例执行成功
        logger.info(f"断言获取到的实际结果为{res}")
        # 问题：截图截不到底部
        # 解决：显式等待，向下滚动，知道看到最后一个记录
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[@class='el-table__row'][last()]")))
        ActionChains(self.driver).scroll_by_amount(0, 10000).perform()
        self.get_screen()
        assert res != []
