'''
Swagger 文档配置
第2种方式：
   定义参数parser=api.parser()
   传递及校验参数@api.expect(parser)或者@namespace.expect(parser)
'''
from flask import Flask,request
from flask_restx import  Resource,Api,Namespace,fields
from werkzeug.datastructures import FileStorage

from python_bg.log_util import logger

app=Flask(__name__)
api=Api(app)

hello_ns=Namespace("demo",description="demo 学习")


@hello_ns.route("")
class Demo(Resource):

    #定义parser解析器
    get_parser=api.parser()
    get_parser.add_argument('id',type=int,location="args",required=True)
    get_parser.add_argument('case_title', type=str, location="args",required=True)
    @hello_ns.expect(get_parser)
    def get(self):
        logger.info((f"requesr.args====>{request.args}"))
        return  {"code":0,"msg":"get success"}


    post_parser = api.parser()
    post_parser.add_argument('file', type=FileStorage, location="files")
    post_parser.add_argument('choice',choices=('one','two'),location="args")
    post_parser.add_argument('param1',help='username',type=str,location="form",required=True)
    post_parser.add_argument('param2',help='password',type=int,location="form",required=True)
    # post_parser.add_argument('param2',type='password',location="json",required=True)
    @hello_ns.expect(post_parser)
    def post(self):
        logger.info((f"requesr.args====>{request.args}"))
        logger.info((f"requesr.args====>{request.files}"))
        logger.info((f"requesr.args====>{request.form}"))
        # logger.info((f"requesr.args====>{request.json}"))
        return {"code": 0, "msg": "get success"}

api.add_namespace(hello_ns,'/hello')

if __name__ == '__main__':
    app.run(debug=True)