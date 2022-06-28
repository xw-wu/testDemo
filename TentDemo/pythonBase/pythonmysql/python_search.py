'''
pymysql 查询
    fetchone():获取单条记录
    fetchmany(n):获取n条记录
    fetchall()；获取所有结果记录
'''
import sys

from pythonBase.pythonmysql.py_mysqldemo import get_conn


def test_search():
    #获取连接
   conn= get_conn()
    #获取游标
   cursor=conn.cursor()
   sql="select * from testcase"
    #捕获异常
   try:
       #执行sql
        cursor.execute(sql)
       #查询记录
       #获取单条记录
        # record=cursor.fetchone()
       #获取N条记录
        # record=cursor.fetchmany(2)
       #获取所有记录
        record=cursor.fetchall()
        print(record)
   except Exception as e:
       #打印错误信息
        print(sys.exc_info())
   finally:
       #关闭链接
        conn.close()