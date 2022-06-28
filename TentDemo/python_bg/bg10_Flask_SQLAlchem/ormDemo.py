'''
Flssk-SQLAlchemy的实例化
官网：http://www.pythondoc.com/flask-sqlalchemy/config.html?highlight=Sqlalchemy_database_url
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
#将app与Flask-SQLAlchemy进行绑定，实例化一个db对象
# db =SQLAlchemy(app)
username="root"
pwd="123456"
ip="127.0.0.1"
port="3306"
database="mysql"

#设置mysql链接方法是
app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
# 设置SQLALCHEMY_TRACK_MoDIFICATIONS参数，不设置会抛出警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
#将app与Flas-SQLAlchemy的db进行绑定
db=SQLAlchemy(app)