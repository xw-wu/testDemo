'''
数据模型
    数据模型（Data Model）是数据特征的抽象，它从抽象层次上描述了系统的静态特征、动态行为和约束条件，为数据库系统的信息表示与操作提供的一个抽象的框架
'''
'''
Flask-SQLAlchemy的属性字段定义
通常类的属性相当于表的一个字段
定义的属性的方式为name=Column（参数的类型，其他的属性）
官方：https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/?highlight=column

参数类型 含义
Integer 整型字段定义
String(20) 字符串字段定义，括号为字符串的最大长度
JSON    json字符串的字段
DateTime    时间格式字段
'''
'''
常用关键字参数
primary_key  是否主键
autoincrement   是否自增
nullable    是否允许为空
unique      是否允许重复
default     默认值
'''