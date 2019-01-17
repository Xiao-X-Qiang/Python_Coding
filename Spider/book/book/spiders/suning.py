
# -*- coding: utf-8 -*-
import scrapy
import re
from copy import deepcopy

# 网站己挂，主要体会实现的逻辑以及数据在方法间的传递

class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        # 大分类
        li_list = response.xpath("/ur[@class = 'ulwrap']/li")  # 大分类列表
        for li in li_list:
            item = {}  # 一个大分类下的所有book共享同一个item
            item["b_cate"] = li.xpath("./div[1]/a/text()").extract_first()
            a_list = li.xpath("./div[2]/a")  # 小分类列表
            for a in a_list:
                item["s_cate"] = a.xpath("./text()").extract_first()
                item["s_href"] = a.xpath("./@href").extract_first()
                if item["s_href"] is not None:
                    item["s_href"] = "http://snbook.suning.com/" + item["s_href"]
                    yield scrapy.Request(
                        item["s_href"],
                        callback=self.parse_book_list,
                        # meta={"item":item}
                        meta={"item": deepcopy(item)}  # 阻止item的传址操作，采用deepcopy操作
                    )

    def parse_book_list(self, response):  # 图书列表页
        item = deepcopy(response.meta["item"])
        li_list = response.xpath("//div[@class='filtrate-books list-filtrate-books']/ul/li")  # 图书列表
        for li in li_list:
            item["book_name"] = li.xpath(".//div[@class='book-title']/a/@title").extract_first()
            item["book_img"] = li.xpath(".//div[@class='book-img']//img/@src").extract_first()
            if item["book_img"] is None:
                item["book_img"] = li.xpath(".//div[@class='book-img']//img/@src2").extract_first()
            item["book_author"] = li.xpath(".//div[@class='book-author']/a/text()").extract_first()
            item["book_press"] = li.xpath(".//div[@class='book-publish']/a/text()").extract_first()
            item["book_desc"] = li.xpath(".//div[@class='book-descrip c6']/text()").extract_first()
            item["book_href"] = li.xpath(".//div[@class='book-title']/a/@href").extract_first()
            yield scrapy.Request(
                item["book_href"],
                callback=self.parse_book_detail,
                # meta={"item":item},
                meta={"item": deepcopy(item)}
            )

        # 图书列表页翻页
        page_count = int(re.findall(r"var pagecount=(.*);", response.body.decode())[0])  # 请求地址不变，内容更新，ajax加载常见的套路
        current_page = int(re.findall(r"var currentPage=(.*);", response.body.decode())[0])
        if current_page < page_count:
            next_url = item["s_href"] + "pageNumber={}&sort=0".format(current_page + 1)
            yield scrapy.Request(
                next_url,
                callback=self.parse_book_list,
                # 目的传大分类、小分类信息,此item只包含大分类、小分类、小分类url地址,注意dict的引用
                meta={"item": response.meta["item"]}
            )

    # 图书详情页提取图书的价格
    def parse_book_detail(self, response):
        item = response.meta["item"]
        item["book_price"] = re.findall(r"\"bp:\":'(.*?)'", response.body.decode())
        item["book_price"] = item["book_price"] if len(item["book_price"]) > 0 else None

        print(item)
