'''
Allure 特性-测试报告中添加附件
    场景：
        希望在报告中看到测试用例的详细内容展示
        比如在用例中添加附件信息，可以是数据，文本，图片，视频，网页
    解决：
        @allure。attache显示许多不同类型的提供的附件，可以补充测试，步骤或测试结果
    用法：
    allure。attach(body(内容))，name，attachment_type,extension
'''