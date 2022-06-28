from flask import Flask, jsonify, render_template, make_response

app=Flask(__name__)

#返回文本信息
@app.route("/text")
def get_text():
    return "返回文本信息"

#返回元组
@app.route("/tuple")
def get_tuple():
    return "你好呀",200,{"hogwarts":"ad"}

#直接用字典返回json
@app.route("/dict")
def get_dict():
    return {"status":0}

#使用jsonify
@app.route("/json")
def get_json():
    return jsonify(status=1,name="ad",age=20)

#返回一个html页面
@app.route('/html/')
def get_html():
    return render_template("demo.html")

@app.route("/more")
def get_more():
    resp=make_response(render_template("demo.html"))
    resp.set_cookie('nameone','thename')
    resp.headers["hife"]="ad2"
    return resp

if __name__ == '__main__':
    app.run()