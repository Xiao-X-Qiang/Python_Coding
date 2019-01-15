
# -*- coding: utf-8 -*-
import scrapy
from onepiece.items import OnepieceItem
import re

# 爬百度贴吧"航海王启航"所有帖子的标题、作者、以及内容的图片链接
class HanghaiwangSpider(scrapy.Spider):
    name = 'hanghaiwang'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?ie=utf-8&kw=航海王启航&fr=search']  #

    def parse(self, response):

        li_list = response.xpath('//div[@class="threadlist_lz clearfix"]')  # 标签，无需extract或extract_first
        for li in li_list:
            item = OnepieceItem()
            # 注意标签属性值在Elements与Network中有可能有不同的显示，可参考幕布 xpath在不同情形下的区别-->4.xpath的坑
            # item["title"] = li.xpath(".//div[@class='threadlist_title pull_left j_th_tit ']/a/@title").extract_first()
            item["title"] = li.xpath("./div[1]/a/@title").extract_first()  # 结果为字符串,并做了异常处理
            item["href"] = "https://tieba.baidu.com" + li.xpath("./div[1]/a/@href").extract_first()

            item["author"] = li.xpath("./div[2]/span/@title").extract_first()
            item["author"] = re.search(r"主题作者: (.*)", item["author"]).groups()[0]  # 正则

            item["content_img"] = []

            # 提交(yield)详情页处理,并附带数据(meta)
            yield scrapy.Request(item["href"], callback=self.content_detail, meta={"item": item})

        # next_url
        next_url = "https:" + response.xpath("//a[text()='下一页>']/@href").extract_first()
        print(next_url)
        yield scrapy.Request(next_url, callback=self.parse)

    def content_detail(self, response):
        item = response.meta["item"]  # 携带而来的数据

        # 当前页的图片列表追回至item["content_img"]列表中
        [item["content_img"].append(i) for i in response.xpath('//img[@class="BDE_Image"]/@src').extract()]

        # next_url
        next_url = response.xpath('//a[text()="下一页"]/@href').extract_first()
        print(next_url)
        if next_url is not None:
            next_url_1 = "https://tieba.baidu.com" + next_url
            # 提交(yield)下一页至详情页处理，并携带数据(meta)  item["content_img"]为列表，可继续追回数据
            yield scrapy.Request(next_url_1, callback=self.content_detail, meta={"item": item})
        else:
            yield item  # 提交至pipelines
