from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 测试的平台是Android
desired_caps['platformVersion'] = '6.0'  # 平台的版本是6.0
desired_caps['deviceName'] = 'mumu127.0.0.1:7555'  # 设备的名字是"mumu127.0.0.1:7555"，设备的名字可以随便起，这边用的是mumu+获取到的名字
# com.android.settings/com.android.settings.Settings
desired_caps['appPackage'] = 'com.android.settings'  # 每个手机都有的"设置"功能，"设置"的包名
desired_caps['appActivity'] = 'com.android.settings.Settings'  # "设置"首页的名字

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 跟服务器建立连接
print("启动【设置】应用")  # 打印一条日志
driver.quit()  # 最后退出
