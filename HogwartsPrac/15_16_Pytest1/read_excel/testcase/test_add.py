import pytest
import openpyxl
from read_excel.func.operation import my_add


def get_excel():
    """
    解析excel数据
    :return: [[1,1,2],[3,6,9],[100,200,300]]
    """
    # 获取工作表
    book = openpyxl.load_workbook("../data/params.xlsx")
    # 获取工作表
    sheet = book.active
    # 读取数据
    cells = sheet["A1":"C3"]
    print(cells)
    values = []
    for row in cells:
        data = []
        for cell in row:
            data.append(cell.value)
        values.append(data)
    print(values)
    return values


class TestWithEXCEL:
    @pytest.mark.parametrize('x,y,expected', get_excel())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
