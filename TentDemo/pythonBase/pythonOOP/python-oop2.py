'''
python 三大特性
    封装：把数据与功能集合在一起
    继承:子类继承父类的属性和方法
    多态：子类可以自己的方法和属性，多个自乐你的方法和属性可能各有不同
面向对象编程优点：解决了系统的可维护性，可扩展性，可重用性。
'''
class Airplan:
    name=''
    color=''

    def set_color(self,color):
        self.color=color
        print(f"飞机的颜色是：{self.color}")

    def set_name(self,name):
        self.name=name
        print(f"飞机的名字是:{self.name}")

# air1=Airplan()
# air1.set_name("第一家飞机")
# air1.set_color("红色")
#
# air2=Airplan()
# air1.set_name("第二家飞机")
# air1.set_color("蓝色")
#类方法里后直接括号里添加父类方法
class CivilAirplan(Airplan):
    def load_person(self,num):
        print(f"民用机的载人数量未：{num}")
    #继承可以改变父类的方法
    def set_name(self,name):
        self.name=name
        print(f"民用飞机的名字是:{self.name}")

class JunAirplan(Airplan):
    name='军用机'
    def set_name(self,name):
        self.name=name
        print(f"当前{self.name}的名字为：{name}")

civiAirplan=CivilAirplan()
civiAirplan.set_name("上海航空一号")
civiAirplan.set_color("民用机的颜色是绿色")
civiAirplan.load_person(100)

jun=JunAirplan()
jun.set_name("军用机1号")
