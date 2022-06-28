import requests


def test_file():
    url="http://127.0.0.1:5000/file"
    file={'file':open(r"D:\C文档\冒烟测试用例.xls",'rb')}
    r=requests.post(url,files=file)

    assert r.status_code==200