import json


def get_json():
    with open("./demo.json", "r", encoding="utf8") as file:
        data = json.loads(file.read())
        print(data, type(data))
        s = json.dumps(data, ensure_ascii=False)  # ensure_ascii=False可以帮助我们去解析中文字符
        print(s, type(s))


if __name__ == '__main__':
    get_json()
