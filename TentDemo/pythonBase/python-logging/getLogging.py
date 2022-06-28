'''
封装日志公共函数参考代码
    http://ceshiren.com/t/topic/13564
'''
import logging
import os


def get_logger():
    #记录器
    logger=logging.getLogger(os.path.basename(__file__))
    logger.setLevel(logging.DEBUG)
    #文件处理器
    ch=logging.FileHandler(filename='myapp.log',encoding='utf-8')
    ch.setLevel(logging.DEBUG)
    #定义格式器
    formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s%(message)s ')
    #将格式器保存到处理器
    ch.setFormatter(formatter)
    #将处理器保存到记录器
    logger.addHandler(ch)
    return logger

logger=get_logger()

def log_info(message):
    logger.info(message)


logger.info('--->info message')
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')