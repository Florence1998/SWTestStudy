import json

import pytest
from read_json.func.operation import my_add


def get_json():
    """

    :return:[[1,1,2],[3,6,9],[100,200,300]]
    """
    with open("../data/params.json") as file:
        data = json.loads(file.read())
        print(data)
        print(data.values())
        print(list(data.values()))
        return list(data.values())


class TestWithJson(object):
    @pytest.mark.parametrize("x,y,expected", get_json())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
