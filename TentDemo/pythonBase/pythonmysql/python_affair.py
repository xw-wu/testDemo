'''
执行事务
    提价操作：commit()
    回滚操作：rollback()
    try-catch-finally
'''
from pythonBase.pythonmysql.py_mysqldemo import get_conn


def test_Insert():
    conn=get_conn()
    cursor= conn.cursor()
    sql="insert into testcase (title,expect,owner) values ('S12群求总决赛','冠军','EDG');"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()