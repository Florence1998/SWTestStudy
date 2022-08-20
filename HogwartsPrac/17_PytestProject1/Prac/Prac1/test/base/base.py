from script.calculator import Calculator


class Base(object):
    def setup_class(self):
        self.cal = Calculator()

    def setup(self):
        print("【开始计算】")

    def teardown(self):
        print("【结束计算】")
