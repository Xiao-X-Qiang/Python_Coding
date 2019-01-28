
from lxml import etree


def main():
    text = ''' <div> <ul> <li class="item-1"><a href="link1.html"></a></li> " 
                                  <li class="item-1"><a href="link2.html">second item</a></li> 
                                  <li class="item-inactive"><a href="link3.html">third item</a></li> 
                                  <li class="item-1"><a href="link4.html">fourth item</a></li>
                                   <li class="item-0"><a href="link5.html">fifth item</a> '''  # 缺少</li>标签

    ret = etree.HTML(text)  # 返回Element对象
    # print(etree.tostring(ret).decode('utf8'))  # lxml自动修正代码补全标签或其它操作，使用etree.tostring()观察修正后的代码

    ret1 = ret.xpath("//li[@class=\"item-1\"]")  # 返回的对象列表
    ret2 = ret.xpath("//li[@class=\"item-1\"]//text()")  # 返回的字符串列表
    ret3 = ret.xpath("//li[@class=\"it1em-1\"]")  # 无匹配项，返回空列表
    # ret1 = ret.xpath("//li[@class=\"item-1\"][2]")  # 返回符合条件的对象列表中的第2个
    print(ret1)
    print(type(ret1))

    # for i in ret1:
    #     item = dict()
    #     item["title"] = i.xpath("./a/text()")[0] if len(i.xpath("./a/text()")) > 0 else None  # xpath()返回结果列表
    #     item["link"] = i.xpath("./a/@href")[0] if len(i.xpath("./a/@href")) > 0 else None
    #     # print(i.xpath("./a/text()"))
    #     # print(item)


if __name__ == '__main__':
    main()
