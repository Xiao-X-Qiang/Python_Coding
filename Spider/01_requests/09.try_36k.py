import requests
import re
import json


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"}
    res = requests.get("https://36kr.com/", headers=headers)

    res = res.content.decode()

    ret = re.findall("<script>var props=(.*?),locationnal", res)[0]  # 截取单个字符口串，

    with open("3.txt", 'w') as f:
        f.write(ret)

    ret1 = json.loads(ret)  # 只能转化单个json字符串，多个的话，一个个来

    print(ret1)


if __name__ == "__main__":
    main()
