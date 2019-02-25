# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymysql import  connect

class TencentPipeline(object):
    def process_item(self, item, spider):
        # return item
        item_list = []
        for i in item:
            item_list.append(item[i])
        self.cursor.execute("insert into position_hr values (0,%s,%s,%s,%s)",item_list)
        self.conn.commit()

    def open_spider(self,spider):
        self.conn = connect(host="localhost",user="root",password="root",port=3306,database="tencent")
        self.cursor = self.conn.cursor()


    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

