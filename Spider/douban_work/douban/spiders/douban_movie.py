# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
import json,copy,re

# 爬取豆瓣电影并存储于Mongdb数据库中

class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=韩国&sort=time&page_limit=20&page_start=0']
    def parse(self, response):
        result = json.loads(response.body_as_unicode())

        len_ = len(result.get("subjects"))
        item = DoubanItem()
        if len_>0:
            for i in range(len_):
                item["id"] = result.get("subjects")[i]["id"]
                item["title"] = result.get("subjects")[i]["title"]
                item["rate"] = result.get("subjects")[i]["rate"]
                item["cover_url"] = result.get("subjects")[i]["cover"]
                next_url = result.get("subjects")[i]["url"]
                yield scrapy.Request(url=next_url,callback=self.parse_item,meta={"data":copy.deepcopy(item)})

            # 下一页数据
            page_num = re.search(r'start=(\d+)',response.url).group(1)
            page_num = "start=" + str(int(page_num)+20)
            next_page = re.sub(r'start=\d+',page_num,response.url)
            yield scrapy.Request(url=next_page,callback=self.parse,dont_filter=True)

    # 详情页数据
    def parse_item(self,response):
        item = response.meta["data"]
        item["director"] = response.xpath("//div[@id='info']/span[1]/span[2]//text()").extract_first()
        item["actor"] = response.xpath("//div[@id='info']/span[2]/span[2]//text()").extract()
        if len(item["actor"])>1:
            temp = []
            for i in range(len(item["actor"])):
                if len(item["actor"][i].strip())>1:
                    temp.append(item["actor"][i].strip())
            item["actor"] = temp
        item["year"] = response.xpath('//span[contains(text(),"上映")]/following-sibling::span[1]/text()').extract_first()
        item["year"] = re.search(r"^(\d+?)-\d",item["year"]).group(1)

        yield item
