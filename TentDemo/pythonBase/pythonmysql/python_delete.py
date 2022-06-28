'''
pythonmysql 删除操作
'''
from pythonBase.pythonmysql.py_mysqldemo import get_conn


def test_delete():
    conn=get_conn()
    cursor=conn.cursor()
    sql="delete from testcase where id=9"
    try:
        cursor.execute(sql)#执行sql
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()