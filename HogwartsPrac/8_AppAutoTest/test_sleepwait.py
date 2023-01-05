import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

desire_caps = {}
desire_caps["platformName"] = "Android"
desire_caps["platformVersion"] = "6.0"
desire_caps["deviceName"] = "127.0.0.1:7555"
desire_caps["appPackage"] = "com.xueqiu.android"
desire_caps["appActivity"] = ".view.WelcomeActivityAlias"
desire_caps["noReset"] = "true"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
# # ===1.强制等待：强制的睡—定的时长,即使后面的页面已经加载出来了
# time.sleep(3)
# ===2.隐式等待：隐式等待一般是在实例化完driver之后设置，它一个全局的等待方式（每一次调用find_element 方法的时候，都会触发隐式等待）
# 隐式等待的缺点:1.让脚本的执行速度整体变慢 2．它只能判断元素存在，是否可点击，是否可用这些属性还不一定存在
driver.implicitly_wait(30)  # 每隔0.5秒查找一次，如果20秒之内查找到了这个元素，后面的的时间就不等了
# ===3.显式等待：判断元素是否处于可点击的状态
WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable(
        (AppiumBy.ID, "com.xueqiu.android:id/tv_search")
    )
)
driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/tv_search").click()
# # ===1.强制等待：操作完成上一个步骤的操作，要等待页面加载出来我们想要的元素，再去操作
# time.sleep(3)
driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.quit()
