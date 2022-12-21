from _pytest.config import Config
from _pytest.config.argparsing import Parser

web_env = {}
# 实现命令行注册，解决自定义参数报错的问题
def pytest_addoption(parser: Parser):
    # 注册一个命令行组
    hogwarts = parser.getgroup("hogwarts")
    # 第一个参数为指定的命令行的参数的形式
    # pytest .\test_demo.py --browser=chrome
    # pytest .\test_demo.py --driver=chrome
    # 注册一个命令行参数
    hogwarts.addoption("--browser", default="firefox", dest="browser", help="指定执行的浏览器")


def pytest_configure(config: Config):
    browser = config.getoption("browser")
    print(f"通过命令行获取到的浏览器为{browser}")
    web_env["browser"] = browser
