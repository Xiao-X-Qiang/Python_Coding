# -*- coding: utf-8 -*-
import scrapy


# 抓取 https://hr.tencent.com/position.php 数据并存入Mysql中 tencent.position_hr数据表中,详情参考 pipelines.py
# mysql> desc position_hr;
# +----------+---------------------+------+-----+---------+----------------+
# | Field    | Type                | Null | Key | Default | Extra          |
# +----------+---------------------+------+-----+---------+----------------+
# | id       | int(10) unsigned    | NO   | PRI | NULL    | auto_increment |
# | title    | varchar(200)        | YES  |     | NULL    |                |
# | type_    | varchar(30)         | YES  |     | NULL    |                |
# | num      | tinyint(3) unsigned | YES  |     | NULL    |                |
# | pub_date | datetime            | YES  |     | NULL    |                |
# +----------+---------------------+------+-----+---------+----------------+
# 5 rows in set (0.00 sec)

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = response.xpath("//form[@id='searchform']/following-sibling::table[1]/tr")[1:-1]
        for tr in tr_list:
            item = {}
            item["title"] = tr.xpath("./td[1]/a/text()").extract_first()
            item["type"] = tr.xpath("./td[2]/text()").extract_first()
            item["num"] = tr.xpath("./td[3]/text()").extract_first()
            item["position_date"] = tr.xpath("./td[5]/text()").extract_first()
            # print(item)
            yield item

        next_url = response.xpath("//a[@id='next']/@href").extract()
        if len(next_url) >0:
            next_url = "https://hr.tencent.com/" + next_url[0]
            yield scrapy.Request(next_url,callback=self.parse)
