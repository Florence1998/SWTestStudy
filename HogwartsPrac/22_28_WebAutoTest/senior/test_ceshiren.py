from selenium import webdriver
from selenium.webdriver.common.by import By


def test_ceshiren_ca():
    # mac
    # capbility = {"platformName": "mac"}
    capbility = {"platformName": "windows"}
    driver = webdriver.Chrome(desired_capabilities=capbility)
    driver.get("https://ceshiren.com/")


def test_ceshiren_grid():
    # 1.本地执行代码调通
    # 2.切换为webdriver.Remote()
    executor_url = "https://selenium-node.hogwarts.ceshiren.com/wd/hub"
    capabilities = {"browserName": "chrome", "browserVersion": "101.0"}
    # driver = webdriver.Chrome()
    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=capabilities)
    driver.implicitly_wait(3)
    driver.get("https://ceshiren.com/")
    login_text = driver.find_element(By.CSS_SELECTOR, ".login-button").text
    print(login_text)  # 1.检查能否打印出文本信息 2.进入hub网站检查状态有无发生变化
