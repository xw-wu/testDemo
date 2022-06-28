from flask import Flask
from flask_restx import  Resource,Api,Namespace

app=Flask(__name__)
api=Api(app)

#定义两个命名空间，对应两个路由
hello_ns=Namespace("demo",description="demo 学习")
case_ns=Namespace("case",description="用例管理")

#将@api.route("/case") 改为@case_ns.route("")
#定义子路由,如果没有的化，就传空
@case_ns.route("")
class User(Resource):
    def get(self):
        return  {"code":0,"msg":"get success"}

    def post(self):
        return {"code": 0, "msg": "post success"}

    def put(self):
        return {"code": 0, "msg": "put success"}

    def delete(self):
        return {"code": 0, "msg": "put success"}

@hello_ns.route("")
class Demo(Resource):
    def get(self):
        return  {"code":0,"msg":"get success"}

    def post(self):
        return {"code": 0, "msg": "post success"}

    def put(self):
        return {"code": 0, "msg": "put success"}

    def delete(self):
        return {"code": 0, "msg": "put success"}


api.add_namespace(hello_ns,'/hello')
api.add_namespace(case_ns,'/case')

if __name__ == '__main__':
    app.run(debug=True)