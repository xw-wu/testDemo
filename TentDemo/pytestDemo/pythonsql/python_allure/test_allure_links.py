import allure

TEST_CASE_LINK='https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/'

@allure.link('https://www.youtube.com')
def test_with_link():
    pass


@allure.link('https://www.youtube.com',name='click me')
def test_with_name_link():
    pass

@allure.issue('140','try agin')
def test_with_issue_link():
    pass

@allure.testcase(TEST_CASE_LINK,'Test case title')
def test_with_testcase_link():
    pass