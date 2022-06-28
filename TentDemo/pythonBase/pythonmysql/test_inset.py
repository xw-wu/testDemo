'''
插入记录
'''
from py_mysqldemo import get_conn

def test_insert():
    conn=get_conn()
    cursor=conn.cursor()
    sql="insert into testcase (title,expect,owner) values ('S14群求总决赛','冠军','EDG');"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()