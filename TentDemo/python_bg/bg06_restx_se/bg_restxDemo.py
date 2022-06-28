from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
#1.创建api实例对象
api = Api(app)
#2.使用api来添加路由
@api.route('/hello')
#类要继承Resource模块
class HelloWorld(Resource):
    #4.定义restful风格的get方法
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'post': 'world'}

if __name__ == '__main__':
    app.run(debug=True)