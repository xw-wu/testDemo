'''
概述
    Python的数据库接口标准是Python DB-API
    PyMySQL是从Python连接到MySQL数据库服务器的接口
    PyMySQL的目标是成为MySQLdb的替代品
    官方文档 http://pymysql.readthedocs.io
'''

'''
pyMysql安装
    使用pip安装 pip install pymysql
    使用Pycharm界面安装
'''
'''
pymysql 连接数据库
    host:mySQL 服务器地址
    user：用户名
    password：密码
    database：数据库名称
    charset：编码方式，推荐使用utf8mb4
'''
'''
pymysql 入门实例
    获取连接对象
        打开
        关闭
    获取游标对象
        执行sql
        查询记录
'''
import pymysql


def get_conn():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        database="bookdb",
        charset="utf8mb4"
    )

    return conn

   # host="localhost",
   #      user="root",
   #      password="123456",
   #      database="bookdb",
   #      charset="utf8mb4"