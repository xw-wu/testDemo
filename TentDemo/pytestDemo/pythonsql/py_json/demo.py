import json


def get_json():
    with open('test.json','r',encoding="utf-8") as file:
        data=json.loads(file.read())
        print(data,type(data))
        s=json.dumps(data,ensure_ascii=False)
        print(s,type(s))
if __name__ == '__main__':
    get_json()