import pytest
import yaml


class TestDemo(object):
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))  # 读取env.yml文件内容
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            print(env)
            print("测试环境的ip是：", env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print(env)
            print("开发环境的ip是：", env["dev"])

    def test_yaml(self):
        print(yaml.safe_load(open("./env.yml")))  # 读取yml文件的内容，查看传过来的是啥格式
