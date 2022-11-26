import time

from selenium.webdriver.common.by import By

from selenium_frame_window.base import Base


class TestFile(Base):
    def test_file_upload(self):
        # 1.打开百度图片网址
        self.driver.get("https://image.baidu.com/")
        # 2.点击"按图片搜索（摄像头）"图标
        self.driver.find_element(By.ID, "sttb").click()
        time.sleep(3)
        # 3.找到"选择文件"按钮，将本地的图片文件上传
        self.driver.find_element(By.ID, "stfile").send_keys("D:/头像.jpg")
        time.sleep(3)
