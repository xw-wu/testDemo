'''
Flask RESTX 集成Swagger
    namespace 的使用
    swagger 接口文档配置
'''
'''
Flask RESTX namespace的使用
    1.定义Namespace实例
    2.为类添加装饰器
        @namespace.route("")控制子路由
    3.为命名空间指定方位路径
        api.add_namespace(case_ns,'/case')
'''
'''
Swagger 文档配置
    第一种：使用@api.doc()或者@namespace.doc()装饰请求方法，例如：
        @api.doc(params={'is':'An ID'})
    第二种【推荐】:使用parser=api.parser()配合@api.expect(parser)装饰器实现入参的校验和传入
'''
'''
api.parser()用法
    格式：api.parser().add_argument(参数名，关键字参数)
    第一个参数是参数名
    后面是关键字传参，常用的关键字有：
        type：类型
        required：约束控制
        choices 枚举参数
        location 对应 request 对象中的属性
'''
'''
常用的关键字参数
    参数名 参数值
    type int,bool,float,string,FileStorage
    required True/False
    choices 枚举
    location args,form,json,files
'''
'''
处理get请求参数 args
'''
'''
处理post请求，json请求
'''
'''
处理post请求， file/form/choice 格式

http json 和form表单互斥
'''