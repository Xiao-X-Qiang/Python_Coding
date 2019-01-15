# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class OnepiecePipeline(object):
    def process_item(self, item, spider):
        if spider.name == "hanghaiwang":  # 判断item来源于哪个爬虫实例
            with open("hanghaiwang_tieba.txt",'a',encoding="utf8") as f:
                f.write(json.dumps(dict(item),ensure_ascii=False))
                f.write("\n")
            print("保存成功",item["title"])
        return item
