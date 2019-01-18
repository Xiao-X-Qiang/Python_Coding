# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class Porn91Pipeline(object):
    def process_item(self, item, spider):
        print(item)
        self.f.write(json.dumps(item, ensure_ascii=False))
        self.f.write("\n")

    def open_spider(self, spider):

        f = open("src_video_url.txt","a",encoding="utf8")
        self.f = f

    def close_spider(self, spider):
        self.f.close()
