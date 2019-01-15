# -*- coding: utf-8 -*-
import scrapy


class Itcast1Spider(scrapy.Spider):
    name = 'itcast1'
    allowed_domains = ['itcast']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):

        return {"title":"this is itcast1"}
