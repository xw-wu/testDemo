from flask import Flask
from flask_restx import  Resource,Api

app=Flask(__name__)
api=Api(app)

#接口路径定义到类上，对应不同请求操作创建不同的方法
@api.route("/case")
class User(Resource):
    def get(self):
        return  {"code":0,"msg":"get success"}

    def post(self):
        return {"code": 0, "msg": "post success"}

    def put(self):
        return {"code": 0, "msg": "put success"}

    def delete(self):
        return {"code": 0, "msg": "put success"}

@api.route("/demo")
class Demo(Resource):
    def get(self):
        return  {"code":0,"msg":"get success"}

    def post(self):
        return {"code": 0, "msg": "post success"}

    def put(self):
        return {"code": 0, "msg": "put success"}

    def delete(self):
        return {"code": 0, "msg": "put success"}


if __name__ == '__main__':
    app.run(debug=True)