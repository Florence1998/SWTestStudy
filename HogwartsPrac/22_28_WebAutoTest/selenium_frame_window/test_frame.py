from selenium.webdriver.common.by import By

from selenium_frame_window.base import Base


class TestFrame(Base):
    def test_frame(self):
        # 1.打开包含frame的web页面
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 2.切换到包含"请拖拽我"元素的frame,打印"请拖拽我"元素的文本
        self.driver.switch_to.frame("iframeResult")  # 未嵌套的frame通过frame的id进行切换
        # self.driver.switch_to_frame("iframeResult") 另一种写法，不常用
        print(self.driver.find_element(By.ID, "draggable").text)
        # 3.切换回默认frame（父级frame），打印“点击运行”元素的文本
        self.driver.switch_to.default_content()
        # self.driver.switch_to.parent_frame()  # 另一种写法
        print(self.driver.find_element(By.ID, "submitBTN").text)
