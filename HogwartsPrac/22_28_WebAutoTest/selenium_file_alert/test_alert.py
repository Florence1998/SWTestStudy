import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium_frame_window.base import Base


class TestAlert(Base):
    def test_alert(self):
        # 1.打开网页https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 2.操作窗口右侧页面，将元素1"请拖拽我!" 拖拽到 元素2"请放置到这里!"
        self.driver.switch_to.frame("iframeResult")
        start_ele = self.driver.find_element(By.ID, "draggable")
        target_ele = self.driver.find_element(By.ID, "droppable")
        ActionChains(self.driver).drag_and_drop(start_ele, target_ele).perform()
        time.sleep(3)
        # 3.这时候会有一个alert弹框，点击弹框中的"确定"
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        # 4.然后再按"点击运行"，元素1"请拖拽我!" 回到原来位置
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "submitBTN").click()
        time.sleep(3)

