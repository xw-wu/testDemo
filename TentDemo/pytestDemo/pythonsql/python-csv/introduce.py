'''
csv 文件介绍
    csv：逗号分隔值
    是Comma-Separated Values的缩写
    以纯文本形式存储数字和文本
    文件由任何数目的记录组成
    每行记录最多由多个字段组成
'''
import csv

'''
读取数据
    内置函数：open（）
    内置模块：csv（）
方法：csv.reader（iterable）
    参数：iterable，文件或列表对象
    返回：迭代其，每次迭代会返回一行数据

'''
'''
    工程目录结构
        data目录：存放csv数据文件
        func目录：存放被测函数文件
        testcase目录：存放测试用例文件
'''
def get_csv():
    with open('demo.csv','r',encoding='UTF-8') as file:
        raw=csv.reader(file)
        for line in raw:
            print(line)

if __name__=='__main__':
    get_csv()