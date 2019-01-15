# -*- coding: utf-8 -*-
import scrapy

from yangguang.items import YangguangItem

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):  # 解析start_urls
        tr_list = response.xpath("//div[@class='greyframe']/table[2]/tr/td/table/tr")
        for tr in tr_list:
            item = YangguangItem()
            item["title"] = tr.xpath("./td[2]/a[@class='news14']/@title").extract_first()
            item["href"] = tr.xpath("./td[2]/a[@class='news14']/@href").extract_first()
            item["publish_date"] = tr.xpath("./td[5]/text()").extract_first()
            print(item)

            # 提交(yield)至详情页方法，并将item传递给详情页(meta)
            yield scrapy.Request(item["href"], callback=self.parse_detail, meta={"item": item})

        # 找寻下一页的地址
        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(next_url,callback=self.parse)  # 提交(yield)至解析页方法parse

    # 处理详情页(与首页的解析方式不同，因而另定义该方法)
    def parse_detail(self, response):
        item = response.meta["item"]
        item["content_img"] = response.xpath('//div[@class="textpic"]/img/@src').extract()
        item["content"] = response.xpath('//div[@class="wzy1"]/table[2]/tr[1]//text()').extract()
        item["content_img"] = ["http://wz.sun0769.com" + i for i in item["content_img"]]
        yield item  # 提交(yield)item至pipelines
