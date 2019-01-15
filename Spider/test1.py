import re

temp = "主题作者：路45341"

if __name__ == "__main__":
    ret = re.search(r"主1题作者：(.*?)53(.*?)", temp)
    print(ret.group())  # 匹配的完整结果
    print(ret.group()[0])  # 匹配的完整结果，同上
    print(ret.group()[1])  # 分组匹配的第一个结果
    print(ret)  # 匹配结果对象，无匹配时为None
    print(type(ret.groups()))  # 分组匹配结果的元组，eg:第一个分组结果：ret.groups[0]

    print("*" * 15)

    ret1 = re.match(r"主题(.*?)41", temp)
    print(ret1.group())
    print(ret1.group()[0])
    print(ret1.group(1)[1])
    print(ret1)

    print(ret1.groups()[0])
