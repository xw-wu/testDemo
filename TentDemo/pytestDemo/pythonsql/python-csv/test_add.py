import csv

import openpyxl
import pytest

from pytestDemo.pythonsql.py_excel.operation import my_add

def get_csv():
    with open('param.csv','r',encoding='UTF-8') as file:
        raw=csv.reader(file)
        r=[]
        for line in raw:
            r.append(line)
        print(r)
    return r



class TestWithExcel:
    @pytest.mark.parametrize('x,y,excepted',get_csv())
    def test_add(self,x,y,excepted):
        assert my_add(int(x),int(y)) == int(excepted)