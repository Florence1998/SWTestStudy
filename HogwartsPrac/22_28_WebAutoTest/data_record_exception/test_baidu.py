import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


# 目标1：实现代码异常的时候，截图/打印page_source
# 实现方法：try catch配合截图/page_source操作
# ===问题1：异常处理会影响用例本身的结果
# 解决方案：在exception之后再把异常抛出
# ===问题2：异常捕获处理代码和业务代码无关，不能耦合
# 解决方案：使用装饰器装饰用例或者相关方法，就不会体现在源码中了（注意：！！！一定要先学习装饰器）

# 1.先把装饰器的架子搭好
# 2.把相关逻辑嵌套进来
# ===问题3：需要通过driver实例截图/打印page_source，装饰器需要先去获取driver对象
# 解决方案：
# ===问题4：隐藏的小bug，一旦被装饰方法有返回值，会丢失返回值
# 解决方案：# 当被装饰方法/函数发生异常就捕获并做数据记录
#             return func(*args, **kwargs)
def ui_exception_record(func):
    def inner(*args, **kwargs):
        # 获取被装饰方法的self，也就是实例对象
        # 通过self就可以拿到声明的实例变量driver
        # 前提条件：1.被装饰的方法是一个实例方法 2.实例需要有实例变量self.driver
        # ===问题：被装饰函数还没有执行，所哟还没有self.driver
        # 解决方案1：获取driver放在函数执行之后
        # 解决方案2：保证使用装饰器的时候，driver已经声明
        # driver = args[0].driver
        try:
            # 当被装饰方法/函数发生异常就捕获并做数据记录
            return func(*args, **kwargs)
        except Exception:
            # 出现异常的处理
            driver = args[0].driver  # 解决方案1：获取driver放在函数执行之后（放在这，兼容性更好一点）
            # print("出现异常啦")
            # 截图操作
            timestamp = int(time.time())
            # 注意!!一定要提前创建好images路径
            image_path = f"./images/image_{timestamp}.PNG"
            page_source_path = f"./page_source/page_source_{timestamp}.html"
            # 截图
            driver.save_screenshot(image_path)
            # 记录page_source
            with open(page_source_path, "w", encoding="u8") as f:
                f.write(driver.page_source)
            # 将截图放到报告的数据中
            allure.attach.file(image_path, name="picture", attachment_type=allure.attachment_type.PNG)
            # 将page_source记录到报告中
            # 如果想要html源码格式使用text，如果想要页面格式就用html
            # allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.HTML)
            allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.TEXT)
            raise Exception

    return inner


class TestBaidu:
    def setup_class(self):
        self.driver = webdriver.Chrome()  # 解决方案2：保证使用装饰器的时候，driver已经声明

    @ui_exception_record
    def test_baidu(self):
        # self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "su1")
        self.driver.quit()
