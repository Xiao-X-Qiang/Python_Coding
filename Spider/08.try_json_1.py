
import json
from pprint import pprint


def main():
    dict1 = {1: "helo",
             2: "world",
             3: "你好"}



    json_tmp = json.dumps(dict1, ensure_ascii=False, indent=2)

    with open("1.txt", "w", encoding="utf8") as f:
        f.write(json_tmp)

    # 使用json.jump将python数据类型放入类文件对象中
    with open("2.txt","w") as f:
        json.dump(dict1, f, ensure_ascii=False, indent=2)

    # 使用json.load提取类文件对象中的数据
    with open('1.txt', 'r', encoding='utf8') as f:
        ret = json.load(f)
        print(ret)
        print(type(ret))


if __name__ == "__main__":
    main()
