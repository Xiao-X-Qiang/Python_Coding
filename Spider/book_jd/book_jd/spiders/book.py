
# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import json
import re


# 爬取京东图书--抓取京东图书包含图书的名字、封面图片地址、图书url地址、作者、出版社、出版时间、价格、图书所属大分类、图书所属小的分类
# 大分类-->小分类-->列表页-->新请求查询价格
#                       -->列表页翻页

# 注意：
# response响应与页面elements页面元素不一致的情况，比如item["p-img"]字段，坑苦我了都
# 对于作者字段列表(可能多个作者)的处理时，先剔除空白字符(空白字符也是有长度的)，然后再可以长度剔除单个列表中的单个元素


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com', 'p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath("//div[@class='mc']/dl/dt")  # 大分类
        for dt in dt_list:
            item = {}
            item["b_cate"] = dt.xpath("./a/text()").extract_first()
            em_list = dt.xpath("./following-sibling::dd[1]/em")  # 小分类
            for em in em_list:
                item["s_cate"] = em.xpath("./a/text()").extract_first()
                item["href"] = em.xpath("./a/@href").extract_first()
                item["href"] = "https:" + item["href"] if len(item["href"]) > 0 else None  # 注意链接的完整性检验

                yield scrapy.Request(
                    item["href"],
                    callback=self.book_list,
                    meta={"item": deepcopy(item)}
                )

    def book_list(self, response):  # 书籍列表页
        item = response.meta["item"]
        li_list = response.xpath("//div[@id='plist']/ul/li")
        for li in li_list:
            item["p_name"] = li.xpath(
                ".//div[@class='p-name']/a/em/text()").extract_first().strip()  # 有空白字符，使用strip(),注意对象必须是字符串

            item["p-img"] = li.xpath(".//div[@class='p-img']/a/img/@src").extract_first()
            if item["p-img"] is None:
                item["p-img"] = li.xpath(
                    ".//div[@class='p-img']/a/img/@data-lazy-img").extract_first()  # response响应与elements不一致
            if item["p-img"] is not None:  # 判断链接是否为None
                item["p-img"] = "https:" + item["p-img"]

            item["p-author"] = li.xpath(".//div[@class='p-bookdetails']/span[1]//text()").extract()
            item["p-author"] = [i.strip() for i in item["p-author"]]  # 去掉左右的空白字符
            item["p-author"] = [i for i in item["p-author"] if len(i)>1]  # 去掉空白字符后才可使用长度进行剔除单个字眼

            # extract() 得到列表--> i.strip() 剔除左右的空白字符  -->len()>1 剔除著、译等单个字眼

            item["p-pub-store"] = li.xpath(
                ".//div[@class='p-bookdetails']//span[@class='p-bi-store']/a/text()").extract_first()
            item["p-pub-date"] = li.xpath(
                ".//div[@class='p-bookdetails']//span[@class='p-bi-date']/text()").extract_first().strip()
            item["data-sku"] = li.xpath("./div[1]/@data-sku").extract_first()

            yield scrapy.Request(  # 查询价格
                "https://p.3.cn/prices/mgets?skuIds=J_{}".format(item["data-sku"]),
                callback=self.book_price,
                meta={"item": deepcopy(item)}
            )

        # 列表页翻页
        next_url = response.xpath("//a[@class='pn-next']/@href").extract_first()
        if next_url is not None:
            next_url = "https:/" + next_url if len(next_url) > 0 else None
        yield scrapy.Request(
            next_url,
            callback=self.book_list,
            meta={"item": deepcopy(item)}
        )

    def book_price(self, response):
        item = response.meta["item"]
        item["p-price"] = json.loads(response.body.decode())[0]["op"]
        print(item)
