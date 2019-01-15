# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']  # 允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 最开始的start_url

    def parse(self, response):
        for i in range(10):
            item = {}
            item["come from "] = "itcast"
            # logging.warning(item)
            logger.warning(item)
            # yield item

        # 处理start_url 对应的响应
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1)
        # pass

        # # 分组
        # li_list = response.xpath("//div[@class='tea_con']//li")
        # for i in li_list:
        #     item = {}
        #     # 方式1  extract()用于获取文本值
        #     # item["name"] = i.xpath(".//h3/text()").extract()[0]  # 取xpath结果列表中所有项的文本的第一个，没有对结果做判断，有别于方式2
        #     # item["title"] = i.xpath(".//h4/text()").extract()[0]
        #     # print(item)
        #
        #     # 方式2：
        #     # item["name"] = i.xpath(".//h3/text()")[0].extract()  # 取xpath结果列表中第一项的文本，没有对结果做判断;下面才是正确的方式(作判断)
        #     # item["title"] = i.xpath(".//h41/text()")[0].extract() if len(i.xpath(".//h41/text()"))>0 else None
        #     # print(item)
        #
        #     # 方式3：
        #     item["name"] = i.xpath(".//h3/text()").extract_first()  # 取xpath结果列表中的第一项;做判断，无结果则为None;取第一项的文本
        #     item["title"] = i.xpath(".//h4/text()").extract_first()
        #     # print(item)
        #     yield item