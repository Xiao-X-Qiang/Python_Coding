# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import urllib
import re


# 对当当网教育目录下所有图书信息的抓取
# 此程序主要用于验证，没有布分布式

class Book1Spider(scrapy.Spider):
    name = 'book_1'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://book.dangdang.com/']

    def parse(self, response):
        div = response.xpath("//div[@class='con flq_body']/div[3]")  # 大分类
        item = {}
        item["b_cate"] = div.xpath("./dl[@class='primary_dl']/dt//text()").extract_first().strip()

        dl_list = div.xpath("./div//dl[@dd_name]")  # 中分类
        for dl in dl_list:
            item["m_cate"] = dl.xpath("./dt/a/text()").extract_first().strip()

            a_list = dl.xpath("./dd/a")  # 小分类
            for a in a_list:
                item["s_cate"] = a.xpath("./@title").extract_first()
                item["href"] = a.xpath("./@href").extract_first()
                # print(item)
                yield scrapy.Request(
                    item["href"],
                    callback=self.parse_book_list,
                    meta={"item": deepcopy(item)}
                )

    def parse_book_list(self, response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@id='search_nature_rg']//li[@ddt-pit]")  # 图书列表
        for li in li_list:
            item["book_name"] = li.xpath("./p[@class='name']/a/text()").extract_first().strip()
            item["book_img"] = li.xpath("./a/img/@src").extract_first()
            item["book_img"] = urllib.parse.urljoin(response.url, item["book_img"])

            item["book_price"] = li.xpath("./p[@class='price']/span[@class='search_now_price']/text()").extract_first()

            item["book_author"] = li.xpath("./p[@class='search_book_author']/span[1]//text()").extract_first()
            if item["book_author"] is not None:
                item["book_author"] = [i.strip() for i in
                                       li.xpath("./p[@class='search_book_author']/span[1]/a/text()").extract()]  # 剔除空白字符
                item["book_author"] = [i for i in item["book_author"] if len(i) > 1]  # 剔除单个字符，比如：空字符、译，著等字眼


            item["book_publish_date"] = li.xpath("./p[@class='search_book_author']/span[2]/text()").extract_first()
            # print(item["book_name"])
            # 正则匹配日期，有的\2018-01-01,有的[2018-02-01],故用正则匹配
            if item["book_publish_date"] is not None:  # 有的图书没有出版日期

                item["book_publish_date"] = re.findall(r"\d{4}-\d{2}-\d{2}", item["book_publish_date"])[0]

            item["book_publish_store"] = li.xpath(
                "./p[@class='search_book_author']/span[3]/a/text()").extract_first()
            if item["book_publish_store"] is not None:
                item["book_publish_store"].strip()
            yield item

        next_url = response.xpath("//a[@title='下一页']/@href").extract_first()
        next_url = urllib.parse.urljoin(response.url, next_url)
        yield scrapy.Request(
            next_url,
            callback=self.parse_book_list,
            meta={"item": deepcopy(item)}
        )
