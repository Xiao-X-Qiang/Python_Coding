
import re

temp = "主题作者：路45341"

if __name__ == "__main__":
    ret = re.match(r"主题作者：(.*?)53(.*)", temp)
    print(ret.group())  # 匹配的完整结果
    print(ret.group(0))  # 匹配的完整结果，同上
    print(ret.group(1))  # 分组匹配的第一个结果
    print(ret)  # 匹配结果对象，无匹配时为None
    print(ret.groups())
    print(type(ret.groups()))  # 分组匹配结果的元组，eg:第一个分组结果：ret.groups()[0]

    print("*" * 15)

    ret1 = re.search(r"主题(.*?)41", temp)
    print(ret1.group())
    print(ret1.group(0))
    print(ret1.group(1))
    print(ret1)

    print(ret1.groups())

    print("*" * 15)

    ret2 = re.findall(r"主题作者：(.*?)53", temp)
    ret2_1 = re.findall((r"主题作者：.*?53"), temp)
    ret3 = re.findall(r"主题作者：(.*?)53(.*)", temp)
    print(ret2)
    print(ret2_1)
    print(ret3)
    # 综上：group与groups的区别：
    # 1. m.group() == m.group(0) == 所有匹配的字符(即匹配正则表达式整体结果)
    # 2. group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分...
    # 3. m.groups() 返回所有括号匹配的字符，以tuple格式。m.groups() == (m.group(0), m.group(1), ...)
    # 4. 没有匹配成功的，re.search（）返回None
    # 5. 正则表达式中没有括号匹配时，group(...)或groups(...)会报错

    # re.match()、re.search() 的结果是一对象(此时，可用groups()或group())或None

    # re.findall() 的结果是一列表：[]、[x1] 或[(x1,x2,...)] x1,x2为匹配的结果(x1可表示多项的集合)
    # eg:ret = re.findall(r'(../info/\d+/\d+.htm)',html) 会匹配html中所有符合条件的url地址，即结果形式为：[x1,x2,x3...]

    # 有括号时，返回分组匹配的结果，无括号时，返回整个匹配结果
