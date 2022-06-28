#get 请求
#需要导入request 对象，不是requests！！
from flask import Flask, request
from python_bg.log_util import logger
app = Flask(__name__)



@app.route("/login",methods=["get"])
def login():
    logger.info(f"请求参数为：{request.args}")
    return {"code":0,"msg":"get success"}

@app.route("/regist",methods=["post"])
def post_regist():
    logger.info(request.json)
    return {"code":0,"msg":"json success"}

#注册、用户名、密码、邮箱
@app.route("/regist1/",methods=["put"])
def post_regist1():
    logger.info(f"请求方法{request.method}")
    logger.info(f"请求url{request.url}")
    usernam=request.form.get("usernam")
    password = request.form.get("password")
    email = request.form.get("email")
    print(f"注册用户的姓名是{usernam}，密码是{password}，邮箱是{email}")
    logger.info(request.form)
    return {"code":0,"msg":"form success"}
#处理文件请求
@app.route("/file/",methods=["post"])
def post_file():
    fileobje=request.files.get("file")
    logger.info(fileobje)
    #文件保存代码
    # request.files.get("file").save("./xx.xls")
    return {"code":0,"msg":"file success"}

if __name__ == '__main__':
    #flash启动起来
    #轮询等待的方式，等待浏览器发来请求
    app.run()