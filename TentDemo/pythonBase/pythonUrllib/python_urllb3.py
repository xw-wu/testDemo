'''
python urllib3
    客户协议端

    功能
        线程安全
        连接池管理
        客户端SSL/TLS验证
        支持HTTP和SOCKS代理
    官方文档
        https://urllib3.readthedocs.io/en/stable
    安装 pip install urllib3
    概述
    内置模块
        urllib
    第三方库
        requests
        urllib3
'''
import json

'''
urllib3 发送http请求
    导入urllib3模块
    创建PoolManager实例
    调用request()方法
'''

'''
urllib3 HTTPResponse 对象
    status 属性
    headers 属性
    data属性
'''
'''
urllib3 解析响应内容
    二进制响应内容解码
    json字符穿
'''
'''
urllib3 request 请求参数
    语法：request(method,url,fields,headers,**)
    必填
        method：请求方式
        url：请求地址
    选填：
        headers：请求头信息
        fields：请求提数据。（可以是form表单或jsob文本）
        body：指定请求体类型
        timeout：设置超时时间
'''
import urllib3

def test_http():

    #创建线程池对象
    ps=urllib3.PoolManager()
    #发送请求
    # res=ps.request(method='GET',url='http://httpbin.org/ip')
    # # print(res.status)
    # # print(res.headers)
    # # print(res.data)
    # # print(type(res))
    # #todo 获取二进制形式的响应内容
    # raw=res.data
    # print(type(raw),raw)
    # #解码成字符穿
    # content=raw.decode('utf-8')
    # print(type(content),content)
    # #json 解析成字典对象
    # obj=json.loads(content)
    # print(type(obj),obj)
    # print(obj['origin'])

    '''
    定制请求头信息
    使用headers参数
    '''
    #定制请求头信息
    headers={'School':'hogwarts'}
    url="http://httpbin.org/get"
    #发动请求
    re=ps.request('GET',url,headers=headers)
    #查看响应信息
    conten=json.loads(re.data.decode('utf-8'))
    print(conten)
    print(conten['headers'])
    '''
    urllib3 定制请求数据
        定制查询字符串参数
        fields参数：适用于Get，HEAD，DELETE请求
        拼接url：使用与post，put请求
    '''

#get/head/delete 请求
def test_querystr_get():
    pm=urllib3.PoolManager()
    url="http://httpbin.org/get"
    # 定义查询字符串
    feil={'School':'hogwarts'}
    #发送请求
    res=pm.request('get',url,fields=feil)
    #查看响应信息
    conte=json.loads(res.data.decode('utf-8'))
    print(conte)

#post/put 请求
def test_urlencode():
    pm=urllib3.PoolManager()

    url="http://httpbin.org/post"
    #从内置库urllib的parse模块导入编码方法
    from urllib.parse import urlencode
    #urlencode编码
    encoded_str=urlencode({'school':'hogwars'})
    # encoded_str = {'school': 'hogwars'}
    #拼接到url中，发送请求
    resp=pm.request('POST',url=url+'?'+encoded_str)
    #查看响应信息
    content=json.loads(resp.data.decode('utf-8'))
    print(content)

'''
    urllib3定制请求数据
        提交form表单数据
        类型'Content-Type':'multipart/form-data'
        请求方式 post/put
'''

#post/put请求
def test_form():
    pm=urllib3.PoolManager()
    url="http://httpbin.org/post"
    fileds={'school':'hogwars'}
    #fileds数据会自动转成form格式提交
    res=pm.request('post',url,fields=fileds)
    # 查看响应信息
    da=json.loads(res.data.decode('utf-8'))
    print(da)

'''
    urllib3定制请求数据
        提交JSON表单数据
        类型'Content-Type':'application/JSON'
        请求方式 post/put
'''
def test_json():
    pm=urllib3.PoolManager()
    url="http://httpbin.org/post"
    #设定请求数据类型
    headers={'Content-Type':'application/json'}
    #json文本数据(格式化json数据)
    json_str=json.dumps({'school':'hogwars'})
    #fileds数据会自动转成form格式提交
    res=pm.request('post',url,headers=headers,body=json_str)
    # 查看响应信息
    da=json.loads(res.data.decode('utf-8'))
    print(da)

'''
    urllib3定制请求数据
        超时时间
            timeout:设置超时时间
            时间单位：秒
            值的格式：float类型
'''
def test_timeout():
    pm=urllib3.PoolManager()
    #访问这个地址，服务器会在3秒后响应
    url="http://httpbin.org/delay/3"
    #设置超时时间
    res=pm.request(method='get',url=url,timeout=4.0)
    assert res.status==200

'''
    urllib3发送HTTPS请求
        HTTPS请求默认需要校验证书
        PoolManager的cert_reqs参数
            CERT_REQUIRED:需要校验
            CERT_NONE:取消校验
'''
def test_https():
    pm_https=urllib3.PoolManager(cert_reqs="CERT_NONE")
    url="https://httpbin.org/get"
    #发动HTTPS请求
    res=pm_https.request(method='get',url=url)
    print(json.dumps(res.data.decode('utf-8')))