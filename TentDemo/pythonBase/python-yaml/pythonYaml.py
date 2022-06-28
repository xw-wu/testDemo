
'''
python 第三方库yaml
    一种数据序列化格式
    用于人类的可读性和脚本语言的交互
    一种被认为可以超宇xml。json的配置文件

'''
'''
yaml 基本语法规则
    大小写敏感
    使用缩进表示层级关系
    缩进时不允许使用Tab键，只允许使用空格
    缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
    #表示注释，从这个字符一致到行尾，都会被解析器忽略
'''
'''
Yaml 支持的数据结构
    对象：键值对的集合，用冒号：表示
    数组：一组按次序排列的值，前加“_”
    纯量：单个的、不可再分的值
        字符串
        布尔值
        整数
        浮点数
        Null
        时间
        日期
    
'''
'''
pyyaml
    python的yaml解析器和生成器
    官网：https://pypi.org/project/PyYAML/
    安装 pip install pyyaml
'''
import yaml
# #创建yaml文件
#
# data={
#   "code": 200,
#   "msg": "成功",
#   "data": {
#     "date": [
#       1653494400,
#       1653580800,
#       1653667200,
#       1653753600,
#       1653840000,
#       1653926400,
#       1654012800
#     ],
#     "series": [
#       {
#         "name": "智联招聘—招聘找工作求职招人软件",
#         "data": [
#           9,
#           8,
#           7,
#           8,
#           8,
#           9
#         ]
#       }
#     ]
#   }
# }
#
# with open('./my.yaml','w',encoding='utf-8') as f:
#   #如果写入内容为中文allow_unicode=True
#     yaml.dump(data,f,allow_unicode=True)
#读取yaml


#读取yaml文件中的内容转化为python文件
with open('./my.yaml','r',encoding='utf-8') as f:
  #如果写入内容为中文allow_unicode=True
    data=yaml.safe_load(f)

print(data)
print(type(data))

#取name

name=data['data']['series'][0]['name']
print(name)
