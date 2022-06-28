'''
Swagger 文档配置
第一种方式：
    在doc中使用params、body等
'''
from flask import Flask
from flask_restx import  Resource,Api,Namespace,fields

app=Flask(__name__)
api=Api(app,version="2.0")

hello_ns=Namespace("demo",description="demo 学习")


@hello_ns.route("")
class Demo(Resource):
    post_model=api.model('PostModel',{
        #required是否为必填项
        'name':fields.String(description='The name',required=True),
        #enum枚举类型 只能选择
        'type': fields.String(description='The object type', enum=['A','B']),
        #min 允许最小值
        'age': fields.Integer(min=0),
    })

    @hello_ns.doc(params={'id':'An ID'})
    def get(self):
        return  {"code":0,"msg":"get success"}

    @hello_ns.doc(body=post_model)
    def post(self):
        return {"code": 0, "msg": "post success"}



api.add_namespace(hello_ns,'/hello')

if __name__ == '__main__':
    app.run(debug=True)