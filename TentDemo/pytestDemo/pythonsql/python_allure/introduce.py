'''
allure 介绍
    allure 是一个轻量级，灵活的，支持多语言的测试报告工具
    多平台的，奢华的report框架
    可以未dev/qa提供详尽的测试报告、测试步骤、log
    也可以未管理层提供high level统计报告
    java语言开发，支持pytest，JavaScript，php，ruby等
    可以集成到jenkins
官方网址：http://allure.qatools.ru
'''

'''
Aillure 安装
    1.安装java（推挤爱你1.8版本）需要培之环境变量
    2.安装Allure2.13（版本以上），需要配置环境变量

下载地址：https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/
    mac/linux:下载tar
    windows：下载zip
配置环境变量：解压后将bin目录加入path环境变量
安装贴：https://ceshiren.com/t/topic/3386
下载的压缩包，解压之后放到非中文目录下，然后将文件夹中的bin目录配置到环境变量path中
配置完毕后，重新打开命令行，执行命令allure --version，能够不报错，显示allure的版本号说明安装配置成功

pycharm上安装allure
执行命令：pip install allure-pytest

allure生成测试报告
第一步：输入下面的命令，执行pytest生成allure的json结果文件
    pytest test_cals.py --alluredir ./report  # ./report 也可以是文件夹的名称
    或者pytest.main(["--alluredir=文件夹的名称",""])
 

第二步：输入下面的命令生成html文件并启动一个服务，通过访问链接浏览html报告：
    allure serve ./report
    
    生成报告后无法自动打开
    
    在开始菜单搜索“默认应用设置”，下方有“选择按协议指定的默认程序”，找到“HTTP”把它选一个默认的浏览器关联即可。
'''
'''

'''