'''
pytest 结合数据驱动Excel
读取Excel文件
    第三方库
        xlrd
        xlwings
        pandas
    openpyxl
    官方文档：https://openpyxl.readthedocs.io/en/stable/
'''
'''
openpyxl库的安装
    安装 pip install openpyxl
    导入 import openpyxl
'''
'''
openpyxl库的操作
    读取工作薄
    读取工作表
    读取单元格
'''
import openpyxl

#获取工作薄
book = openpyxl.load_workbook('param.xlsx')
#读取工作表
sheet=book.active
#读取单个单元格
cell_a1=sheet['A1'].value
print(cell_a1)
cell_a3=sheet.cell(column=1,row=3)
print(cell_a3)
#读取多个连续单元格
cells=sheet["A1":"C3"]
#获取单元格的值
print(type(cells),cells)

'''
报错异常：文件打开方式有误，重新创建新的文件
param.xlsx
  Traceback (most recent call last)
  in _find_workbook_part     raise IOError("File contains no valid workbook part")
'''
