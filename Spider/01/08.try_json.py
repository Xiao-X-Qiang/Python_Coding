
import json
from pprint import pprint


def main():
    dict1 = {1: "helo",
             2: "world",
             3: "你好"}

    json_tmp = json.dumps(dict1, ensure_ascii=False, indent=2)
    json_tmp1 = str(dict1)
    json_tmp2 = eval(json_tmp1)

    with open("1.1.txt", "w", encoding="utf8") as f:
        f.write(json_tmp)

    with open("1.txt", 'wb') as f:
        f.write(json_tmp.encode("gbk"))

    ret1 = json.loads(json_tmp)

    pprint(ret1)






if __name__ == "__main__":
    main()
