# 导入 pip install appium-python-client
from appium import webdriver

# 创建一个字典，desirecapbility
caps = {}
caps["platformName"] = "Android"
# Android 包名和页面名，获取命令：
# Mac/Linux: adb logcat ActivityManager:I | grep “cmp"
# Windows: aapt dump badging wework.apk  | findstr launchable-activity
caps["appPackage"] = "io.appium.android.apis"
caps["appActivity"] = ".ApiDemos"
caps["deviceName"] = "127.0.0.1:7555"  # 设备名，一个标识，取啥名都行
# caps["ensureWebviewsHavePages"] = True  # 老师演示的时候直接删了，也没说啥
# 创建driver，与appium server建立连接，返回一个session
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# el1：点击 OS ，进入下一个页面
el1 = driver.find_element_by_accessibility_id("OS")
el1.click()  # 调用点击方法
# el2：点击 Morse Code
el2 = driver.find_element_by_accessibility_id("Morse Code")
el2.click()
el3 = driver.find_element_by_id("io.appium.android.apis:id/text")
el3.clear()
# 调用sendkeys方法，输入ceshiren.com
el3.send_keys("ceshiren.com")
# 返回
driver.back()
# 返回
driver.back()
# 回收session
driver.quit()
                                    