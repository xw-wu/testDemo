'''
python 内置类装饰器
    类方法，classmethod
        不用实例化，直接调用
    静态方法，staticmethod
        提升代码的可读性

'''


'''
普通方法
    定义：第一份参数为self，代表实例本身
    调用：要有实例化的过程，通过实例  对象.方法名 调用
'''


# 1.定义
class MethodsDemo:
    # 类变量
    param_a = 0

    # 定义一个方法，第一个参数必须为self
    def normal_demo(self):
        print('这个一个普通方法', self.param_a)



# #1.调用
# md=MethodsDemo()
# md.normal_demo()
    '''
    类方法
        定义：
            1.使用@classmethod装饰器，第一个参数为类本身，所以通常使用cls，命名做区分（非强制）
            2.在类内可以直接是用类方法或类变量，无法直接使用实例变量或方法
        调用：
            无需实例化，直接通过类.方法名调用，也可以通过实例，方法名调用
    '''

    # 定义类方法必须添加classmethod装饰器
    @classmethod
    def classthod_demo(cls):
        #类方法的第一个参数改成cls
        cls.normal_demo()
        print('这个一个类方法', cls.param_a)
#类的调用
# MethodsDemo.classthod_demo()#无需实例化，直接调用

# #1.调用
# md=MethodsDemo()
# md.normal_demo()
# md.classthod_demo()

    '''
        静态方法
            定义：
                使用@staticmethod装饰器，没有和类本身有关的参数
                无法直接使用任何类变量、类方法、或者实例方法、实例变量
            调用：
                无需实例化，直接通过类.方法名调用，也可以通过实例.方法名调用
    '''
    @staticmethod
    def static_demo(pa):
        print("静态方法",{pa})

# #1.调用
MethodsDemo.static_demo("test1")
st=MethodsDemo()
st.static_demo("test2")

'''
普通方法、类方法、静态方法区别
    定义：
        普通方法：至少需要一个self参数
        类方法：至少需要一个cls参数
        静态方法：无默认参数
    调用：
        普通方法：实例名.方法名（）
        类方法：类名.方法名（）|实例名.方法名（）
        静态方法：类名.方法名（）|实例名.方法名（）
    关键词：
        普通方法：无
        类方法：@classmethod
        静态方法：@staticmethod
    使用场景：
        普通方法：方法内部涉及到实例对象属性的操作
        类方法：如果需要对类属性，即静态变量进行限制性操作
        静态方法：无需类或实例参与
'''

'''
实际案例：类方法
    对输入日期进行格式统一，不修改构造函数的前提
'''
class DateFormat:
    def __init__(self,year=0,month=0,day=0):
        self.year=year
        self.month=month
        self.day=day

    def out_date(self):
        return f"输入的时间为{self.year}年，{self.month}月，{self.day}日"

    @classmethod
    def json_format(cls,json_data):
        #输入一个字典格式的数据信息，返回一个元组
        year, month, day = json_data["year"], json_data["month"], json_data["day"]
        return cls(year,month,day) #=return DateFormat(year,month,day)

#     # "year,month,day=2017,7,1"
# def json_format(json_data):
#         year,month,day=json_data["year"],json_data["month"],json_data["day"]
#         return year,month,day
#
# #json 格式
# year,month,day=json_format({"year":2022,"month":12,"day":1})
# demo=DateFormat(year,month,day)
''''''''
# json_data={"year":2022,"month":12,"day":1}
# demo=DateFormat.json_format(json_data)
#
#
# print(demo.out_date())
'''
静态方法实际案例
    此方法没有任何和实例、类相关的部分，可以作为一个独立函数使用
    某些场景下，从业务逻辑来说又属于类的一部分
    例子：简单工厂方法（设计模型）
'''

class Game:
    def __init__(self,first_hero,second_hero):
        self.first_hero=first_hero
        self.second_hero=second_hero

    #fight有和实例变量交互的部分，所以需要定义成为一个普通方法
    def fight(self):
        print(f"本轮比赛开始由{self.first_hero}VS{self.second_hero}")
    #start 没有和类或实例交互的部分，那么就可以使用staticmethod
    @staticmethod
    def start():
        print("游戏开始")
Game.start()
game1=Game("bob","coc")
game2=Game("nick","mimi")
game1.fight()
game2.fight()

# #static使用场景
# class HeroFactory:
#     #staticMethod 使用场景
#     #方法所有涉及到的逻辑都没有使用实例方法或者实例变量的时候
#     #伪代码
#     @staticmethod
#     def create_hero(hero):
#         if hero =="ez":
#             return EX()
#         elif hero =="jinx":
#             return JINX()
#         elif hero =="timo":
#             return TIMO()
#         else:
#             raise Exception("此英雄不在英雄工厂当中")