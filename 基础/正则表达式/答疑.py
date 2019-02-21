import re
temp = "主题作者：路45341"
if __name__ == '__main__':
    ret = re.match(r"主题作者：(.*?)53(.*)",temp)
    print(ret.group())  # 匹配的完整结果
    print(ret.group(0))  # 匹配的完整结果，同上
    print(ret.group(1))  # 分组匹配的第一个结果
    print(ret)  # 匹配结果对象，无匹配时为None
    print(ret.groups())
    print(type(ret.groups()))  # 分组匹配结果的元组，eg:第一个分组结果：ret.groups()[0]

    print("*"*15)

    ret2 = re.findall(r"主题作者：(.*?)53",temp)
    ret2_1 = re.findall(r"主题作者：.*?53",temp)
    ret3 = re.findall(r"主题作者：(.*?)53(.*)",temp)

    print(ret2)
    print(ret2_1)
    print(ret3)

    # 综上所述：group()与groups()的区别参考脑图
    # re.match()及re.search()的结果是None或对象(此时可用group()或groups())
    # re.findall()的结果是列表:[]、[x1]、[(x1,x2)] ,x1,x2为匹配的结果(x1可表示多项的集合)，可参考脑图
    # 有括号时，返回分组匹配的结果；无括号时，返回整个匹配结果
