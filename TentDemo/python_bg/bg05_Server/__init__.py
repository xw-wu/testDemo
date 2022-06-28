'''
服务启动配置
    监听的主机
    监听的端口
    Debug模式
'''
'''
监听的主机
    设置host参数
    127.0.0.1只能本机访问
    0.0.0.0服务发布到局域网或者直接配置公网IP
    app.run(host="0.0.0.0")
     app.run(host="10.10.1.69",port=5000,debug=True)
    debug :监听代码是否有改变并且重启服务
'''
'''
Debug 模式
    设置debug=True(默认是production)
        实现热加载
        开发调试方便
'''