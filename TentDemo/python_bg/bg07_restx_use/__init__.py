'''
Flask REST接口使用
    设计框架的原则（23种设计模式 6大设计原则）
        复用性
        高内聚（复用性），低耦合（扩展性）
    编写RESTFUL风格的接口
    添加路由的方式
'''

'''
添加路由的两种方式
    方式一：装饰器
        route('/login','/login1')方法
    方式二：api的add_resource()方法
        api.add_resource(Login,'/login','/login1')
'''
'''
高耦合示例
问题：判断条件过多，业务逻辑非常复杂
示例：---反例
示例：
@app.route("/testcase",methods=["GET","PUT","POST"])
def select_case():
    if request.method=="GET":
        pass
    elif request.method=="put":
        pass
'''

'''
低内聚示例
问题：同一个路径，对应多个请求方法，代码没有复用
示例：---反例
@app.route("/login",methods=["get"])
def login():
    return {"code":0,"msg":"get success"}
@app.route("/login",methods=["post"])
def post_regist():
    return {"code":0,"msg":"json success"}

'''