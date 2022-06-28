'''
Fixture 特点及优势
    1.命令灵活：对于setup，teardown，可以不起这两个名字
    2.数据共享：在conftest.py 配置里写方法可以实现数据共享，不需要import导入。可以跨文件共享
    3.scope的层次及神奇的yield组合相当于各种setup和teardown
    4.实现参数化

'''
'''
Fixture 的用法总结
    模拟 setup，tearqown（一个用例可以引用多个fixture）
    yiele的用法
    作用域（session module,类别，方法级别）
    自动执行（autouse参数）
    conftest.py的用法，一般会把fixture卸载conftest.py 文件中（这个名字是固定的，不能改）
    实现参数化
'''

'''
Fixture 在自动化中的应用-基本用法
场景
    测试用例执行时，有的用例需要登陆才能执行，有些用例不需要登陆。
    setup和teardown无法满足。fixture 可以。默认scope（范围）function
    步骤
        1.导入pytest
        2.在登陆的函数上面加@pytest.fixture()
        3.在要使用的测试方法中传入（登陆函数名称），就先登陆
        4.不传入的就不登陆直接执行测试方法
'''
'''
fixture 在自动化中的应用-作用域
    function 函数级 每一个函数或方法都会调用
    class 类级别   每个测试类只运行一次
    module 模块级  每一个.py文件调用一次
    package 包级  每一个python包只调用一次（暂不支持）
    session 会话级 每次会话只需要运行一次，绘画内所有方法及类，模块都共享这个方法
'''


'''
yeid 关键字
    场景：
        已经可以将测试方法【前要执行的或依赖的】解决了
        测试方法后销毁清楚数据的要如何进行呢？
    解决：
        通过在fixture函数中加入yield关键字，yield是调用第一次返回结果，
        第二次执行它下面的语句返回
    步骤：
        在@pytest。fixture（scope=module）
        在登录的方法中加yield，之后加销毁清除的步骤
'''
'''
fixture 在自动化中的应用-数据共享
    场景：
        你与其他测试工程师合作一起开发时，公共的模块要在不同文件中，要在大家都访问到的地方。
    解决：
        使用conftest.py这个文件进行数据共享，并且他可以放在不同位置起着不同的范围共享作用
    前提：
        conftest文件名是不能换的
        放在项目下是全局的数据共享的地方
    执行：
        系统执行到参数login时先从本模块中查找是否又这个名字的变量时什么的
        之后在conftest.py中找是否有
    步骤：
        将登录模块带@oytest.fixture写在conftest.py
'''
'''
fixture-自动应用
    场景：不想原测试方法有任何改动，或全部都自动实现自动应用，没特例，也都不需要返回值时可以选择自动应用
    解决：使用fixture中参数autouse=True实现
    步骤：在方法上面加@pytest.fixture（autouse=True）
'''
'''
fixture-参数化
    场景：
        测试离不开数据，为了数据灵活，一般数据都是通过参数传的
    解决：
        fixture 通过固定参数 request传递
    步骤：
        在 fixture中增加@pytest.fixture(params=[1,2,3,'linda'])
        在方法参数写 request，方法体里面使用request.param接收参数
'''
