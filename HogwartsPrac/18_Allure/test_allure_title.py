import allure


class TestSearch(object):
    @allure.title("搜索词为Android")
    def test_case1(self):
        print("case1")

    @allure.title("搜索词为iOS")
    def test_case2(self):
        print("case2")
