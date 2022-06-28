'''
Flssk-SQLAlchemy的实例化
官网：http://www.pythondoc.com/flask-sqlalchemy/config.html?highlight=Sqlalchemy_database_url
'''
import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

app=Flask(__name__)
#将app与Flask-SQLAlchemy进行绑定，实例化一个db对象
# db =SQLAlchemy(app)

# with open("./data.yml") as f:
#     result=yaml.safe_load(f)
#     username=result.get('database').get('username')
#     password=result.get('database').get('password')
#     server=result.get('database').get('server')
#     db=result.get('database').get('db')

username="root"
pwd="123456"
ip="127.0.0.1"
port="3306"
database="world"

#设置mysql链接方法是
app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
# 设置SQLALCHEMY_TRACK_MoDIFICATIONS参数，不设置会抛出警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
#将app与Flas-SQLAlchemy的db进行绑定
db=SQLAlchemy(app)

#定义数据库的表，需要继承db,model,db为app启动时的SQLALCHEMY绑定的实例
class World(db.Model):
    id=Column(Integer,primary_key=True)
    username=Column(String(80))

class Office(db.Model):
    #指定表名__tablename__属性
    # __tablename__ = "自定义表名"
    id=Column(Integer,primary_key=True)
    username=Column(String(80))

if __name__ == '__main__':
    # db.create_all()
    db.drop_all()