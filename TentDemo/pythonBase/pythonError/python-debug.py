'''
程序调试
    程序调试是将编制的程序投入实际运行钱，用手工或编译程序等方法进行测试，修正【语法错误和逻辑错误】的过程
    语法错误
        编写的python语法不正确，程序编译失败
    逻辑错误
        代码本身能够正常执行，但是执行完成的结果不符合预期结果
    bg_http
        隐藏在程序中未被发现的缺陷或问题同城为bug
'''
import logging

'''
调试方法
    对应位置使用print 或者logging打印日志信息
    启动断点模式debug调试
'''
logging.basicConfig(level=logging.INFO)
a,b=1,2
if a==1:
    flag=True
    logging.info(f"a==1:flag={flag}")
    logging.error("fewgreg")
else:
    flag=False
print(flag)