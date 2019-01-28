
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider


class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    redis_key = 'mycrawler:start_urls'  # 从redis中获取该键对应的值，可自定义命名

    # allowed_domains = ["amazon.cn","xxx.com"]

    rules = (
        # follow all links
        Rule(LinkExtractor(), callback='parse_page', follow=True),
    )

    def __init__(self, *args, **kwargs):  # 获取允许爬取的域名范围，可与allowed_domains择留其一
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MyCrawler, self).__init__(*args, **kwargs)

    def parse_page(self, response):  # 对于Rule()中提取链接请求获得响应的处理；被Rule()中的callback指定；且方法名不能为parse(...)
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
