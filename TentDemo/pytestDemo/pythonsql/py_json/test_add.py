import csv
import json

import openpyxl
import pytest

from pytestDemo.pythonsql.py_excel.operation import my_add

def get_json():
    with open('param.json','r',encoding="utf-8") as file:
        data=json.loads(file.read())
        print(list(data.values()))
    return list(data.values())

class TestWithExcel:
    @pytest.mark.parametrize('x,y,excepted',get_json())
    def test_add(self,x,y,excepted):
        assert my_add(int(x),int(y)) == int(excepted)