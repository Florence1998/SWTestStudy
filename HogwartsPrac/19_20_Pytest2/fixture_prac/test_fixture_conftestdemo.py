# login方法在conftest模块中定义好了，这里就不需要“import conftest”了
def test_search(login):  # 不需要再传入login参数
    token, username = login
    print(f"token:{token},name:{username}")
    print("搜索")


def test_get_product(connectDB):
    print("验证 获取单品信息")


def test_cart():  # 传入login参数，就会先执行login函数
    print("购物车")


def test_order():
    print("下单功能")


class TestDemo:
    def test_case1(self):
        print("case1")

    def test_case2(self):
        print("case2")
