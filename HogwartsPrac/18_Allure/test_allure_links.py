import allure

TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'


@allure.link('https://ceshiren.com')
def test_with_link():
    pass


@allure.link('https://www.baidu.com', name='百度地址')
def test_with_named_link():
    pass


@allure.issue('5715', 'bug地址')
def test_with_issue_link():
    pass


@allure.testcase(TEST_CASE_LINK, '测试用例管理平台地址')
def test_with_testcase_link():
    pass
