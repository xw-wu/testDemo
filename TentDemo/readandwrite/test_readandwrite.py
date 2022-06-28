import csv
import random


class TestReadAWrite:

    def test_readfile(self):
        with open('D:\\工作\接口测试文档\\test\\data\\gp_appId.csv','r',encoding='utf-8') as f:
            raw = csv.reader(f)
            # ra=[10,20,30,40,50,60,70,80,90,100]

            for r in ra:
                print(r)
                data = []
            # for ra in raw:
            #     print(row)