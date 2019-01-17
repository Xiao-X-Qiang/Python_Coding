# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ElectroItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cate1 = scrapy.Field()
    cate2 = scrapy.Field()
    name = scrapy.Field()
    href = scrapy.Field()
    price = scrapy.Field()

    pass
