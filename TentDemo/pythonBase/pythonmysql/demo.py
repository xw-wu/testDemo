from pythonBase.pythonmysql.py_mysqldemo import get_conn


def test_demo():
    #1.打开链接
    conn=get_conn()
    #2.获取游标
    cursor=conn.cursor()
    #3.执sql
    cursor.execute("SELECT VERSION();")
    #4.获取结果
    version=cursor.fetchone()
    print(version)
    #5.关闭数据库连接
    conn.close()