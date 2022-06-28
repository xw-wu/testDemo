'''
allure 用法
官网：https://docs.qameta.io/allure/#_pytest
源码example：http://github.com/allure-examples/allure-examples
'''
'''
Allure 用法
    @allure.epic()  epic模块：定义项目、当有多个项目是使用，往下是feature
    @allure.feature() 模块名称：用例按照模块区分，有多个模块时给每个起名字
    @allure.story()用例名称：用例的描述
    @allure.title 用例标题：用例标题
    @allure.testcase() 用例相关链接：自动化用例对应的功能用例存放系统的地址
    @allure.issue()缺陷地址：对应缺陷管理系统里面的缺陷地址
    @allure.description()用例描述：对测试用例的详细描述
    @allure.step()操作步骤：测试用例的操作步骤
    @allure.severity()用例等级：blocker、critical、normal、minor、trivial
    @allure.link()定义连接：用于定义个需要再测试报告中展示的连接
    @allure.attachment()附件：添加测试报告附件
'''

'''
Allure 特性-feature/story
    场景： 希望再报告中看到测试功能，子功能或场景
    解决：@Feature，@story
    步骤：
        import allure
        功能上加@allure.feature（‘功能名称’）
        子功能上加@allure.story（‘子功能名称’）
    运行：
        ‘pytest 文件名 --allure-features=FEATURES_SET--allure-stories=STORIES_SET’
        
    feature / story 的关系
        feature 相当于一个功能，一个大的模块，相当与于 testsuite
        story相当于对应的这个功能或这模块下的不同长江，分支功能
        feature于story类似于父子关系
'''

'''
Allure特性-step
    场景：
        测试过程中每个步骤，一般放在具体逻辑方法中，可以放在关键步骤中，在报告中红显示在app，web自动测试当中，建议每切换到一个新的页面当作一个step
    解决：
        with allure.step():可以放在测试用例方法里面，但是测试步骤代码需要被该语句包含
'''
'''
Allure特性-link()、issue()、testcase()
    场景：测试报告中，添加用例的链接，bug链接地址，相关的链接地址
    解决：
        @allure.link()、@allure.issue()、@allure.testcase()
        主要事为了将allure报告和测试管理系统继承（用例管理/bug管理），可以更快速的跳转到公司内部地址
'''
'''
Allure特性-设置优先级
    五种级别：
        BLOCKER("Blocker") 阻塞缺陷（功能未实现，无法下一步）
        CRITICAL（"critical"）严重缺陷（功能点缺失）
        NORMAL（"normal"）一般缺陷（边界情况，格式错误）
        MINOR（"minor"）次要缺陷（界面错误于UI需求不符）
        TRIVIAL（“trivial”）轻微缺陷（必须项无提示，或者提示不规范）
        
    场景：
        通常测试有PO、冒烟测试、验证上线测试。
        按重要性级别来分别执行的，比如腰包主流和重要模块都跑一遍。
    解决
        也可以通过allure。serverity来附加标记
    实例：
        在方法.函数和类上面加
        @allure.severity（allure，serverity_level.TRIVIAL）
    运行：
        运行级别未：normal.criterial 的测试用例
    pytest -s -v 文件名 --allure-severities nomal,critical -alluredir=./result
'''

'''
Allure 总结
支持多平台
java语言开发的，支持多语言pytest，javascript，php，ruby等
可以为dev/qa提供详尽的测试报告、测试步骤、log、标题、优先级、附件等等
也可以为管理层提供high level统计报告
可以集成到Jenkins，展示项目的趋势图 
'''

'''
allure 常用命令
    运行pyrest用例
        pytest --alluredir（包含json txt格式中间格式）
    生成在线版本测试报告
        allure serve 命令
    生成最终版本测试报告
        allure generate命令
        
        
    查看allure一些常用格式 allure --help
    
命令格式 allure [option] [command] [command options]
    在测试执行期间执行结果
        pytest [测试文件] -s -q --alluredir=./result/ （-alluredir这个选项，用于指定存储测试结果的路径）
    查看测试报告
        方式一：测试完成后，查看实际报告，在线看报告，会直接打开默认浏览器展示当前报告
            allure serve ./resul/ （注意这里serve书写）
        方式二：从结果生成报告，这是一个启动tomcat的服务，需要两个步骤：生成报告，打开报告
            生成报告
                allure generate ./result/ -o ./report / --clean (注意：覆盖路径加--clean)  [生成文本在allure-report文件中]
            打开报告
                allure open -h 127.0.0.1 -p 8883 ./report/
'''