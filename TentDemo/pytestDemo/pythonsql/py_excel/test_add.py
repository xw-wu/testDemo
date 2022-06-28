import openpyxl
import pytest

from pytestDemo.pythonsql.py_excel.operation import my_add

def get_excel():
    book=openpyxl.load_workbook('param.xlsx')
    sheet=book.active
    cells=sheet["A1":"C3"]
    print(cells)
    values=[]
    for row in cells:
        data=[]
        for cell in row:
            data.append(cell.value)
        values.append(data)
    print(values)
    return values

class TestWithExcel:
    @pytest.mark.parametrize('x,y,excepted',get_excel())
    def test_add(self,x,y,excepted):
        assert my_add(int(x),int(y)) == int(excepted)