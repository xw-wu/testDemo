import yaml
from flask import Flask, request
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

from web_demo.log_util import logger

app=Flask(__name__)
api=Api(app)

with open("./data.yml") as f:
    result=yaml.safe_load(f)
    username=result.get('database').get('username')
    password=result.get('database').get('password')
    server=result.get('database').get('server')

    db=result.get('database').get('db')

app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://{username}:{password}@{server}/{db}?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db=SQLAlchemy(app)

#创建用例表
class Testcase(db.Model):
    #表名
    __tablename__="testcase"
    #用例ID 用例得唯一标识
    id=db.Column(Integer,primary_key=True)
    #用例得标题或者文件名,限定80个字符，不为空，且唯一
    case_title=db.Column(String(80),nullable=False,unique=True)
    #备注
    remark=db.Column(String(120))

class TestCaseServer(Resource):
    def get(self):
        '''
        测试用例的查找
        :return:
        '''
        logger.info("get method")
        return {"code":0,"msg":"get success"}

    def post(self):
        '''
        测试用例的新增
        :return:
        '''
        case_data=request.json
        logger.info(f"{case_data}")
        logger.info("post method")
        return {"code":0,"msg":"post success"}


if __name__ == '__main__':
    db.create_all()