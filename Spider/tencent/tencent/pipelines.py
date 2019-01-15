# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from tencent.items import TencentItem  # 当前执行的目录为tencent项目，以绝对方式导入

client = MongoClient()
collection = client["tencent"]["hr"]


class TencentPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            print(item)
            collection.insert(dict(item))  # mongodb中只能插入字典
            return item


