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
# class World(db.Model):
#     id=Column(Integer,primary_key=True)
#     username=Column(String(80))

class User(db.Model):
    #指定表名__tablename__属性
    __tablename__ = "user"
    id=Column(Integer,primary_key=True)
    #unique=true 设置唯一
    username=Column(String(80),unique=False)
    email=Column(String(80),unique=True)
    gender=Column(String(3),unique=False)

    def __repr__(self):
        return f"<user {self.username},{self.gender},{self.email}>"

if __name__ == '__main__':
    # db.create_all()
    # db.drop_all()

    #添加数据
    # user1=User(username="hogew",email="123@12.cd",gender="男")
    # user2 = User(username="杨振", email="1231d@12.cd", gender="女")
    # user3 = User(username="岐黄", email="123d2@12.cd", gender="男")
    # #第一种添加
    # db.session.add(user2)
    # db.session.add(user3)
    #第二种添加db.session.add_all(列表)
    # db.session.add_all([user2,user3])
    # db.session.commit()
    # db.session.close()


    #查询全部数据
    # res=User.query.all()
    # for re in res:
    #     print(re.username,re.email)

    #查询单条数据
    # res=User.query.filter_by(gender="男").first()
    # print(res)
    # 查询多条数据
    # res=User.query.filter_by(gender="男").all()
    # print(res)

    # 查询多条件单条数据
    # res=User.query.filter_by(gender="男").filter_by(email="123d2@12.cd").first()
    # print(res)
    # # 查询多条件多条数据
    # res=User.query.filter_by(gender="男").filter_by(username="李四").all()
    # print(res)

    #第一种修改方式,更新某个字段
    # res=User.query.filter_by(id=1).first()
    # res.gender="女"
    # db.session.commit()
    # db.session.close()

    #给定查询条件进行查询后, 直接进行update操作
    # User.query.filter_by(id=1).update({"gender":"男"})
    # db.session.commit()
    # db.session.close()

    '''
    删除数据
        方式一：
            查询数据
            对查询出来的数据对象进行删除操作
            提交session
    '''
    res = User.query.filter_by(id=1).first()
    db.session.delete(res)
    db.session.commit()
    db.session.close()
    '''
        方式二：
            给定查询条件进行查询后，直接进行delete操作
            提交session
    '''
    res = User.query.filter_by(id=3).delete()
    db.session.commit()
    db.session.close()