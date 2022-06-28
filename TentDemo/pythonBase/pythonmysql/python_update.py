
'''
pymysql 更新操作
    更新数据表的数据
'''
from pythonBase.pythonmysql.py_mysqldemo import get_conn


def test_update():
    conn=get_conn()
    cursor=conn.cursor()
    sql="update testcase set owner='hogwarts' where id=2"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()