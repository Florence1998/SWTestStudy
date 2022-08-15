import openpyxl

# 获取工作簿
book = openpyxl.load_workbook("./params.xlsx")

# 获取工作表
sheet = book.active

# 获取单元格数据
a_1 = sheet["A1"].value
print("A1:", a_1)
c_2 = sheet.cell(column=3, row=2).value
print("c2:", c_2)

# 获取多个单元格
cells = sheet["A1":"c3"]
print(type(cells), cells)
