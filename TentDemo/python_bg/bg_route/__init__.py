'''
测试平台介绍
    价值
        测试服务化
            场景：多种测试、多种环境、颗粒度细致
            持续交付（Jenkins 也难以满足）
        测试智能化
            图像分析 机器学习 人工智能
            基于图形的自动化测试，测试用例自动生成
            精准化测试，基于用户使用习惯自动去执行修正测试用例
        测试中台化
            形成测试闭环，对于产品线上问题达到信息同步
'''
'''
测试平台价值
    市场需求：测试平台的开发目前是测试行业中的一个热门的技术
    公司需求：
        能为团队带来市场价值，如果wetest
        高效的平台做调度中心
    例子：
        DevOps平台
        精准化测试平台
        质量监控平台等等
'''
'''
测试平台-前提
    已有的开源测试平台不能满足需要，不要轻易造轮子
    测试的体系健全
    当体系、测试技术等游刃有余，构建平台展示带动整个团队甚至团队之前的其他团队
    当公司级别的定制，不如整合公司内部的多套平台
'''
'''
测试平台基本功能
    用户管理
        注册/登录
    用例管理
        用例导入/管理用例
    任务管理
        执行任务/报告管理
'''
'''
常用的技术架构与组件
    前端技术架构：bootstrap、vue、react
    后端技术架构：django、flask、spring boot
    数据存储：myswl es
    任务调度架构： jenkins
    数据报表：echarts、vega、kibana、grafana、allure
'''
'''
常见的测试平台开发模式
    大而全
        python Django
        java spring boot
        React（前端框架）
    小而简
        python flask
        java sparkjava
        vue
'''

'''
--------------------------------------------
'''
'''
接口与路由技术
    Flask环境安装
    定义路由
'''
'''
定义：
    Flask 是一个轻量级的web开发框架。依赖jinjia2和werkzeugWSGI服务的一个微型框架
环境准备：pip insall flask
    中文文档：
    http://docs.jinkan.org/docs/flask
    英文文档：
    https://flask.palletsprojects.com/en/2.0.x

'''

'''
两种运行方式
    代码调用
        app.run()

    命令行运行
        bash（mac/linx）
        cmd(windows)
        powershell(windows)
'''
'''
定义路由
    通过装饰器@app.route添加路由
    @app.route("/hogwarts")
    def deno2():
    return "<p>Hello, World!</p>"
'''
'''
动态路由
    通过
    app.route('/user/<username>')添加动态路由
    #添加动态路由
    @app.route("/user/<username>")
    def deno2(username):
    return "<p>Hello, World!</p>"    
'''
'''
限定类型
    路径中添加<类型：变量名>来限定变量的类型
    @app.route('/post/<int:post_id>')

    string (缺省值)接受任何不包含斜杠的文本
    int 接受正整数
    float   接受正浮点数
    path    类似string，但可以包含斜杠
    uuid 接受uuid字符串
'''
'''
地址尾部的“/”
路由的尾部带有“/”(浏览器的地址栏中输入和不输入的“/”的效果一样)
路由的尾部没有/（输入的URL的结尾不能加/ 会报错）
'''
'''
window 启动虚拟环境
set FALAK_APP=flaskDemo.py
.\myproject\venv\Scripts\activate

'''