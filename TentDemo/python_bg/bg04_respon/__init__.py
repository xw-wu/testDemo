'''
处理响应信息
    文本型
    元组
    json
    html
    额外数据
'''
'''
返回文本
    @app.route('/text')
    def get_text():
        return '返回文本'
'''
'''
返回元组
    返回元组
        response,status
        response,headers
        response,status,headers
    响应状态码为200
    
    @app.route('/tuple')
    def tuple_res():
        return "你也呀"，200，{"hgowaf":"ad"}
'''

'''
返回json
    第一种方式：直接返回dict会转换为json
        @app.route('/dict')
        def get_dict():
            return {'status':0}
       
    第二种方式：使用jsonify()方法，通过参数传入键值对
        @app.route('/json')
        def get_json():
            #jsonify({'status':0})
            return jsonify(status=1,name="ad",age=20)
'''

'''
返回html
    使用模板渲染技术
    html文件必须在同级的templates
    
    def get_html():
        return render_template('demo.html')

<!--
html文件必须在templates目录下
/application.py
/templates
    /hello.html
-->     
<html>
    <body>
        <hi>霍格我自测试开发</hi>
    </body>
</html>
'''

'''
设置额外数据返回-make——response()
    添加更多的响应信息
    设置cookie
    设置响应头信息等
    
    def index():
        resp=make_response(render_template('demo.html'))
        resp.set_cookie('usernamee','the username')
        resp.headers["hogwarts"]="ad2"
        return resp
'''