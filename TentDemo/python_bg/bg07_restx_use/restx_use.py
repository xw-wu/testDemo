'''
RESTful 风格接口

'''
from flask import Flask
from flask_restx import Api, Resource

app =Flask(__name__)

api=Api(app)

#装饰器
#@api.route("/user","/user1")
#api的add_resource()方法

class User(Resource):
    def get(self):
        return  {"code":0,"msg":"get success"}

    def post(self):
        return {"code": 0, "msg": "post success"}

    def put(self):
        return {"code": 0, "msg": "put success"}

    def delete(self):
        return {"code": 0, "msg": "put success"}

api.add_resource(User,'/user','/user1')
if __name__ == '__main__':
    app.run(debug=True)



