# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()  # 豆瓣ID
    title = scrapy.Field()  # 电影名称
    year = scrapy.Field()  # 上映年份
    region = scrapy.Field()  # 上映地区
    cover_url = scrapy.Field()  # 海报链接
    director = scrapy.Field()  # 导演
    editor = scrapy.Field()  # 编剧
    actor = scrapy.Field()  # 演员
    type = scrapy.Field()  # 影视类型
    language = scrapy.Field()  # 语言
    date = scrapy.Field()  # 上映日期
    run_time = scrapy.Field()  # 片长
    rate = scrapy.Field()  # 评分
    rating_num = scrapy.Field()  # 参与评分人数

