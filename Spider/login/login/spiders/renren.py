# -*- coding: utf-8 -*-
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/969328524/profile']

    def start_requests(self):  # 覆盖父类scrapy.Spider的start_requests请求start_urls的方法(添加cookies后再请求)
        cookies_str = "anonymid=jr1hzy6hiv42sx; depovince=GW; _r01_=1; ick_login=6cd25c22-ff6e-4cd6-a688-48eb726c7f55; first_login_flag=1; ln_uact=17623702688; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; JSESSIONID=abcLj4gr5dzMX6aeDdFHw; wp_fold=0; jebecookies=a0653959-353e-4cd4-8845-71eb3c6b733c|||||; _de=292313AA6F309B3C75AC6BB1D7847ADE; p=4e4032f6c820f05762775555c75c68584; t=1a94190263d538663a4831f4a3370bae4; societyguester=1a94190263d538663a4831f4a3370bae4; id=969328524; xnsid=9fbee024; ver=7.0; loginfrom=null"
        # cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies_str.split("; ")}  # 字典生成式
        headers = {"cookies":cookies_str}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,  # 交由self.parse()方法处理响应
            # cookies=cookies  # request请求中添加cookies参数
            headers = headers
        )

    def parse(self, response):
        ret1 = re.findall(r"(张强)", response.body.decode())
        print(ret1)

        yield scrapy.Request(
            # 请求该url时，会自动地携带上次的cookies信息(settings中的COOKIES_ENABLED默认为True)
            "http://www.renren.com/969328524/profile?v=info_timeline",
            callback=self.parse_detail
        )

    def parse_detail(self, response):
        ret1 = re.findall("重庆理工", response.body.decode())
        print(ret1)
