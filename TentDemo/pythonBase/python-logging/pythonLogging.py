'''
python 日志
    日志作用
        调试
        辅助定位问题
        数据分析
    日志的级别
        DEBUG   细节信息，仅当诊断问题时使用
        INFO    确认程序按预期运行
        WARNING(默认级别) 表明已经或即将发生的意外（例如：磁盘控件不足）。程序仍按预期进行。
        ERROR   由于严重的问题，程序的某些功能已经不能正常执行
        CRITICAL  严重的错误，表明程序已不能继续执行
    日志的用法
        参考文档：https://docs.python.org/zh-cn/3/howto/logging.html
'''
# import logging
# #设置logging级别，最开始的时候调用
# #设置哪个级别会打印这个级别以上日志
# logging.basicConfig(level=logging.INFO)
#
# logging.warning('Watch out!')  # will print a message to the console
# logging.info('I told you so')  # will not print anything
# logging.error('这是一条error信息')  # will not print anything

'''
设置日志的级别

'''
import logging
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

#时间格式处理
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p ')
# logging.warning('is when this event was logged.')

#
logging.basicConfig(filename='myapp.log',
                    level=logging.INFO,
                    format='%(asctime)s[%(levelname)s]%(message)s(%(filename)s:%(lineno)s)',
                    datefmt='%m/%d/%Y %I:%M:%S %p ')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')