#1.导入flask 模块
from flask import Flask
#2.创建Fiask 应用程序的实例
app = Flask(__name__)

#添加路由
#http://ceshiren.com/search?q=appuim
#https---协议
#ceshiren.com ---host域名
#/search --路由
# ?q=appium --请求参数
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/demo")
def deno():
    return "<p>Hello, World!</p>"

@app.route("/user/<int:username>/")
def deno2(username):
    return f"这是{username}同学的个人信息"

#
# @app.route("/user/<int:username>")
# def deno2(username):
#     return f"这是{username}同学的个人信息"


# 启动入口
if __name__ == '__main__':
    #flash启动起来
    #轮询等待的方式，等待浏览器发来请求
    app.run()