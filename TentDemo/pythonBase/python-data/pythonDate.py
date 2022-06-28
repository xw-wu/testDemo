'''
日期函数
    获取当前日期/获取特定时间
    datetime与timestamp时间戳互转
    datetime与str互转
    实战练习
试用场景
    作为日志信息的内容输出
    计算某个功能的执行时间
    用日期命名一个日志文件的名称
    生成随机数（时间是不会重复的）
'''
'''
处理时间的模块
    time
    datetime
    calendar
'''
'''
常见的时间表示形式
    时间戳
    格式化的时间字符串
'''
'''
datetime 常用的类
    datetime 时间日期相关
    timedelta 极端两个时间的时间差
    timezone 时区相关
'''
import  datetime
now=datetime.datetime.now()
print(now)
print(now.day)
#转成时间戳
t=now.timestamp()
print(t)

'''
字符串和时间互转
参考链接：http://docs.python.org/3/library/datetime.html?highlight=strftime
'''
s="2022-05-28 19:06:40"
s1=datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
print(s1)
n=datetime.datetime.now()
resu=n.strftime('%a, %b %d %H:%M')
print(resu)

'''
时间戳与时间互转
'''

ts=1653909668.78854
#时间戳转换为时间
ss=datetime.datetime.fromtimestamp(ts)
print(ss)
#时间转换为时间戳
print(ss.timestamp())
