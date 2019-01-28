
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

# 爬取amazon下的所有图书信息
# 反爬处理：下载中间件中在请求头中加入随机的User-Agent,并作了简单的IP代理(几个简单的IP代理，付费或独享代理有待于进一步完善)

class AmazonBookSpider(RedisCrawlSpider):  # 继承于RedisCrawlSpider,有别于CrawlSpider
    name = 'amazon_book'
    allowed_domains = ['amazon.cn']  # 与__init__() 择留其一
    # start_urls = ['http://amazon.cn/']
    redis_key = "amazon"

    rules = (
        # 匹配大分类及小分类，follow为True,因为大分类与小分类的页面结构雷同
        Rule(LinkExtractor(restrict_xpaths=('// *[@id="leftNav"]/ul[1]/ul/div/li',)), follow=True),
        # xpath中是一列表或元组:(xxx,)

        # 图书列表页，提取链接发送请求后的响应(callback指定的方法处理)中不需要继续提取链接，故而follow=False
        Rule(LinkExtractor(restrict_xpaths=('//div[@id="mainResults"]//h2/..',)), callback='parse_page', follow=False)
    )

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        return i

    def parse_page(self, response):  # 处理数据时，要对提取链接的完整性、及提取数据是否为None(后继的strip()或split()对于None对象会报错)进行判断
        item = {}                    # 编写xpath时尽可能做到精准且通用(部分页面的元素可能变更，比如book-img的属性值)
        item["book_name"] = response.xpath("//span[@id='productTitle']/text()").extract_first()
        if item["book_name"] is None:
            item["book_name"] = response.xpath("//span[@id='ebooksProductTitle']/text()").extract_first()
        item["book_url"] = response.url
        item["book_img"] = response.xpath("//div[@id='img-canvas']/img/@src").extract_first()
        if item["book_img"] is None:
            item["book_img"] = response.xpath("//div[@id='ebooks-img-canvas']/img/@src").extract_first()
        item["book_price"] = response.xpath('//span[@class="a-size-base a-color-secondary"]/text()').extract()
        item["book_author"] = response.xpath('//*[@id="bylineInfo"]/span[@class="author notFaded"]/a/text()').extract()
        item["b_cate"] = response.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[1]/span/a/text()').extract_first().strip()
        item["m_cate"] = response.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[3]/span/a/text()').extract_first().strip()
        item["s_cate"] = response.xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[5]/span/a/text()').extract_first().strip()
        print(item)  # 可在settings中打开pipelines设置(可被RedisPipeline方法保存至redis中)yield item可写入redis
