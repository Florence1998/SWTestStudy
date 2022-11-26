import time

from selenium.webdriver.common.by import By

from selenium_frame_window.base import Base


class TestWindows(Base):
    def test_window(self):
        # 1.打开百度页面，点击“登录”按钮，出现登录弹框
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "s-top-loginbtn").click()
        time.sleep(3)
        # 查看当前所有的句柄以及当前的句柄
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)
        # 2.弹框中点击“立即注册”按钮，跳转到新页面
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__regLink").click()
        # 查看当前所有的句柄以及当前的句柄
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)  # 仍在第1个页面
        # 3.切换到新页面(即第2个页面)，新页面输入用户名和手机号
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__userName").send_keys("翟羽佳995")
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__phone").send_keys("15195383763")
        time.sleep(3)
        # 查看当前所有的句柄以及当前的句柄
        print(self.driver.window_handles)
        print(self.driver.current_window_handle)  # 仍在第1个页面
        # 4.返回刚才的登录页，输入用户名和密码，点击登录
        self.driver.switch_to.window(windows[0])
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__userName").send_keys("15195383763")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys("123zyj")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__submit").click()
        time.sleep(3)
