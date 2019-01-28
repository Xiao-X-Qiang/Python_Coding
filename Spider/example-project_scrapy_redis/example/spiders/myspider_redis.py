
from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    redis_key = 'myspider:start_urls'  # 从redis中获取该键对应的值，可自定义命名

    # allowed_domains = ["amazon.cn","xxx.com"]

    def __init__(self, *args, **kwargs):  # 获取允许爬取的域名范围，可与allowed_domains择留其一
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):  # 对于第一次请求响应的处理
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
