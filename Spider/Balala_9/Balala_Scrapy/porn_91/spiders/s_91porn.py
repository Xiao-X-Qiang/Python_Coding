# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import re


# 该爬虫可以爬取所有视频的地址并保存在video_url.txt文件中

# 大体思路如下：视频列表页提取每个视频所在的网址url，后请求每个url地址在其详情页内正则提取视频的url地址
# 为了获得中文响应，在下载中间件部分添加了Accept、Accept-Language字段，否则获得的响应是英文的
# 为了避免频繁打开或关闭文件，在pipelines中定义了open_spider()及close_spider()方法，程序中断可能会丢失数据

# (为了避开10个限制，在下载中间件部分添加了X-Forwarded-For 字段，即不断更新请求头的IP地址)
# 由于Scrapy的settings中默认开启了cookies跟随(当次的request请求会携带上一次的cookies)，需要将其设为False

class S91pornSpider(scrapy.Spider):
    name = 's_91porn'
    allowed_domains = ['91porn.com']
    start_urls = ['http://www.91porn.com/v.php?next=watch']

    def parse(self, response):
        # with open("a.html","a",encoding="utf8") as f:
        #     f.write(response.body.decode())
        div_list = response.xpath("//div[@id='videobox']//div[@class='listchannel']")
        for div in div_list:
            item = {}
            item["title"] = div.xpath("./a/@title").extract_first()
            item["href"] = div.xpath("./a/@href").extract_first()

            # 视频详情页url
            # yield item

            # 解析视频地址url
            yield scrapy.Request(
                item["href"],
                callback=self.video_url,
                meta={"item": item}
            )

        next_url = response.xpath("//a[text()='»']/@href").extract_first()
        if next_url is not None:
            next_url = "http://www.91porn.com/v.php" + next_url
        yield scrapy.Request(next_url, callback=self.parse)

    def video_url(self, response):
        item = response.meta["item"]
        item["href"] = re.findall(r'<source src="(.*?)" type=\'video/mp4\'>', response.body.decode())[0]
        # item["href"] = re.findall(r'<source src="(.*?)" type=\'video/mp4\'>',str(response.body, 'utf-8', errors='ignore'))
        yield item
