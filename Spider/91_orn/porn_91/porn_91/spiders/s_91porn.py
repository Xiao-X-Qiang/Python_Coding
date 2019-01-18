# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy


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

            yield item

        next_url = response.xpath("//a[text()='»']/@href").extract_first()
        if next_url is not None:
            next_url = "http://www.91porn.com/v.php" + next_url
        yield scrapy.Request(next_url, callback=self.parse)

