import datetime
import time


def timer(func):
    def inner():
        # 第二步，在内函数添加装饰器的逻辑
        print("函数开始执行")
        st=datetime.datetime.now()
        func()  # 第六步添加被装饰函数的执行步骤
        et=datetime.datetime.now()
        print(et-st)

    # 第三步，装饰器的使用
    return inner


@timer
def hogwarts():
    print("霍格沃兹测试学社")


hogwarts()
