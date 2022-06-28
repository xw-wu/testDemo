'''
处理请求数据
    get请求参数
    json请求
    表单请求
    文件请求
request 对象
    官方网址：https://dormousehole.readthedocs.io/en/latest/api.html#incoming-request-data
'''
'''
request 的常用属性/方法
    属性/方法 说明
    args    记录请求中查询参数
    json    记录请求中的json数据
    files   记录请求上传的文件
    form    记录请求中的表单数据
    method  记录请求使用的http方法
    url     记录请求的url地址
    host    记录请求的域名
    headers 记录请求的头信息
'''

'''
浏览器与服务器的请求步骤
    1.接受请求
    2.解析清秀，处理请求
    3.将处理的结果返回回去
日志封装参考地址：https://ceshiren.com/t/topic/13564
'''
'''
args 普通参数处理
    场景 普通的url链接，接受一个get请求
    解决方法 request.args
'''
'''
json 参数处理
    场景 相关的请求，带有json数据格式
    解决方法    request.json
'''
'''
表单请求
    场景：测试人网站的登录接口，需要用户名和密码，前端会提交一个form表单给后台
    解决办法 request.form
'''
'''
文件请求
    场景：
        页面上有个更新头像的功能，或者上传一个excel文件的功能，允许我们提交一个图片，或者文件到后端服务器
    解决方法：
        request.files.get('file')获取文件对象
        filename获取文件对象的文件名
        save() 方法 保存文件到指定路径下
'''