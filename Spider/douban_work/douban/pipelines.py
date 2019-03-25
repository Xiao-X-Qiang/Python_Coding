# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

client = MongoClient()
collection = client["douban"]["movie"]


class DoubanPipeline(object):
    def process_item(self, item, spider):
        print("电影信息：",item)
        collection.insert(dict(item))  # 存储于Mongodb数据库中
        return item
