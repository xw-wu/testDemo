'''
SQLAlchemy 是python中最有名的ORM框架：在Flask——SQLAlchemy来操作数据库
    安装命令 pip install flask-sqlalchemy
'''

'''
Flssk-SQLAlchemy的实例化
官网：http://www.pythondoc.com/flask-sqlalchemy/config.html?highlight=Sqlalchemy_database_url
'''
'''
常用配置
    SQLALCHEMY_DATABASE_URL 链接数据库URL配置
        连接字符串格式：
            dialect+driver://username:password@host:port/database
        常用的sqlite与mysql：
            sqlite：sqlite：///数据库db文件所在的路径
            mysql：mysql+pymysql：//username:password@host:port/database
    SQLALCHEMY_TRACK_MODIFICATIONS  追踪对象的修改
    SQLALCHEMY_BINDS    用于多数据库链接的配置
    SQLALCHEMY_POOL_SIZE    连接池的配置默认为5
'''
'''
SQLALCHEMY 借助数据库中间件操作数据库
    mysql：pymysql  需要安装pymysql
    oracle：cx-oracle 
'''
