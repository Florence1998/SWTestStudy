from selenium import webdriver


class Base(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()
