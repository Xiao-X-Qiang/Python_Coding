# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class Porn91Pipeline(object):
    def process_item(self, item, spider):  # 输出item到文件
        print(item)
        self.f.write(json.dumps(item, ensure_ascii=False))
        self.f.write("\n")

        self.f_only_url.write(item["href"] +'\n')


    def open_spider(self, spider):

        f = open("video_url.txt","a",encoding="utf8")
        f_only_url = open("only_url.txt",'a',encoding="utf8")
        self.f = f
        self.f_only_url = f_only_url

    def close_spider(self, spider):
        self.f.close()
        self.f_only_url.close()
