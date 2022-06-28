#get 请求
from flask import Flask
app = Flask(__name__)

#methods是一个列表，可以添加多种 请求方式，get，post，put
# @app.route("/testcase",methods=["get","post","put","delete"])
@app.route("/testcase",methods=["get"])
def get_case():
    return{"code":0,"msg":"get sucess"}

@app.route("/testcase",methods=["post"])
def post_case():
    return{"code":0,"msg":"post sucess"}

@app.route("/testcase",methods=["put"])
def put_case():
    return{"code":0,"msg":"put sucess"}

@app.route("/testcase",methods=["delete"])
def delete_case():
    return{"code":0,"msg":"delete sucess"}

if __name__ == '__main__':
    #flash启动起来
    #轮询等待的方式，等待浏览器发来请求
    app.run()