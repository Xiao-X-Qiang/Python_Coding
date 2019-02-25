
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import json


class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['cqut.edu.cn']
    start_urls = ['http://www.cqut.edu.cn/index/xxyw.htm']

    rules = (
        # LinkExtractor:链接提取器：提取url地址
        # callback:提取的url经请求后的响应会交由callback指定的方法进行处理
        # follow:LinkExtrator提取的url经请求后的响应是否再次被rules提取，默认False

        # 大致过程表述为：start_urls-->请求并得到响应-->rules中Rule1对响应提取url-->请求并得到响应-->交由callback指定的方法处理
        #                                        -->rules中Rule2对响应提取url-->请求并得到响应-->交由callback指定的方法处理

        #  提取页面的url地址，并依次请求，得到响应后交由parse_item方法处理，且follow为False,即响应内容不再提取
        Rule(LinkExtractor(allow=r'../info/\d+/\d+.htm'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'(xxyw/)?\d+.htm'),follow=True),  # 提取下一页的地址，并再次请求，且follow为True，即响应内容再次提取
    )

    def parse_item(self, response):  # 对于响应，获得页面的具体内容
        item = {}
        item["url"] = response.url
        item["title"] = response.xpath("//div[@class='contitle']/h21/text()").extract_first()

        item["date"] = re.findall(r'日期：(20\d{2}-\d{2}-\d{2})',response.body.decode())[0] if len(re.findall(r'日期：(20\d{2}-\d{2}-\d{2})',response.body.decode()))>0 else None
        # with open("log.txt","a",encoding="utf8") as f:
        #     f.write(json.dumps(item,ensure_ascii=False))
        #     f.write("\n")
        print(item)



