# -*- coding: utf-8 -*-
import scrapy
from suning.items import ElectroItem
import json


class ElectroSpider(scrapy.Spider):
    name = 'electro'
    allowed_domains = ['suning.com']
    start_urls = ['https://shop.suning.com/70079390/list_210409385_1.html']

    def parse(self, response):
        cate1_list = response.xpath("//div[@class='sf-category']/dl/dt")  # 一级类别selector列表

        for cate in cate1_list:
            item = ElectroItem()
            item["cate1"] = cate.xpath("./a/@title").extract_first()  # 一级类别名

            index1 = cate1_list.index(cate) + 1

            cate2_all = response.xpath("//div[@class='sf-category']/dl/dd[{}]".format(index1))  # 一级类别对应的二级类别selector对象

            cate2_list = cate2_all.xpath("./a")  # 二级类别具体的列表，以标签a 标识每一2级类别
            for cate2 in cate2_list:
                item["cate2"] = cate2.xpath("./@title").extract_first()
                item["href"] = cate2.xpath("./@href").extract_first()
                print(item)
                # 由于地址请求信息是js，无以继续，以下为伪代码

                yield scrapy.Request(item["href"], callback=self.process_detail, meta={"item": item})

    def process_detail(self, response):

        item = response.meta["item"]  # 获取传递的数据

        goods_list = response.xpath(...)
        for goods in goods_list:

            # 方式一：如果响应是html的话
            item["name"] = goods.xpath(...)
            item["price"] = goods.xpath(...)

            # 方式二：如果响应是json的话
            item["name"] = json.loads(response)[...]
            item["price"] = json.loads(response)[...]

            yield item  # 保存单个商品信息


        # next_url
        next_url = response.xpath(...)

        # 如果下一页和第一页的处理方式相同；
        # 另根据保存方式的不同，是单个商品信息进行保存，还是一个类别的信息进行保存的不同，方法间数据的传递也会有所不同，可参考爬虫项目--onepiece
        yield scrapy.Request(next_url,callback=self.process_detail,meta={"item":item})

    pass
