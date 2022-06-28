from pythonBase.pythonmysql.py_mysqldemo import get_conn
'''
创建记录
'''

def test_creat():
    conn=get_conn()
    cursor=conn.cursor()
    sql="""
     CREATE TABLE testcase(
    id int(11) NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) COLLATE utf8_bin NOT NULL,
    expect VARCHAR(255) COLLATE utf8_bin NOT NULL,
    owner VARCHAR(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY(id)
    )ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE =utf8mb4_bin;
    """
    cursor.execute(sql)
    conn.close()