'''
两种编程思想
    面向过程
        一种以过程为中心的编程思想
        简单的事情
    面向对象（00P）
        一种更符合我们人类思维习惯的编程思想
        面向对象开发就是不断的创建对象，使用对象，操作对象做事情
        复杂的事情
'''
'''
面向对象
    语言层面，封装代码和数据
    规格层面，对象是一系列可被使用的公共接口
    概念层面，对象是某种拥有责任的抽象
'''
'''
面向对象程序设计规则
    首先分析有哪些类
    每个类有哪些属性和行为
    类与类之间存在的关系
'''
#创建类:通过class定义了一个类
class Persion:
    name="default"
    age=0
    gender='male'
    weight=0

    def __init__(self,name,age,gender,weght):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weght
        # print("init funcion")
    # def set_param(self,name,age,gender,weght):
    #     self.name=name
    #     self.age=age
    #     self.gender=gender
    #     self.weight=weght
    # # def set_age(self,age):
    #     self.age=age
    @classmethod
    def eat(self):
        print(f"name={zs.name} eating")

    def play(self):
        print( f"name={zs.name} playing")

    def jump(self):
        print(f"name={zs.name} jump")

zs=Persion('zhangsan',20,'男',130)
# zs.set_param('zhangsan',20,'男',130)
# zs.set_age(25)
zs.jump()
# print(f"name={zs.name}，age={zs.age}")

'''
类、实例、方法、变量
    类：抽象的概念，一类事物。
    方法：类中定义的函数，对外提供的服务。
    类变量：李变量在整个实例化的对象中是公用的。
    实例引用：实例化一个对象
    实例变量：以’self.变量名‘的方式定义的变量
'''
#类变量和实例变量的区别,类变量需要类来访问，实例变量需要实例来访问
#类变量
Persion.name='lisi'
print(Persion.name)
#实例变量
zs=Persion('zhangsan',20,'男',130)
print(zs.name)

#类方法和实例方法,类方法不能访问，实例方法可以访问
#若要类方法可以访问，需要添加装饰器 @classmethod
print(Persion.eat())
zs=Persion('zhangsan',20,'男',130)
print(zs.eat())
