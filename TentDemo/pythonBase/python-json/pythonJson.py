'''
JSON
    JSON是用于存储交换的数据语法，是一种轻量级的数据交换格式
    使用场景
        接口数据参数
        序列化
        配置文件
'''
'''
JSON结构
键值对形式
数组形式
'''
'''
python与json数据类型对应
    字典
        python dict
        json object
    序列
        python list，tuple
        json    array
    字符串
        python  str
        json    string
    数字类型
        python int，float
        json    number
    布尔值True
        python  True
        json    true
    布尔值False
        python  False
        json    false  
    空值
        python  None
        json    null 
'''
'''
json 库
    可以从字符串或文件中解析json
    该库解析json后将其转换为python字典或者列表
'''
'''
常用方法
    dumps():将python对象编码成json字符串
    loads()；解码JSON数据，该函数返回Python对象
    dump()：Python对象编码，并将数据写入json文件中
    load（）：从json文件中读取数据并解码为python对象
'''
import json
data=[{'a':1,'b':2,'c':True,'d':False,'c':None}]
#将python对象编码为json字符串
json_data=json.dumps(data)
print(json_data)
#将JSON字符串解码为Python对象
python_data=json.loads(json_data)
print(python_data)
#写入JSON数据，在代码当前生成一个data.json的文件
with open('data.json','w') as f:
    json.dump(data,f)
#读取数据，读取json文件并解码成python对象
with open('data.json','r') as f:
    data=json.load(f)
print(data)