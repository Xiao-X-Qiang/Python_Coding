# -*- coding: utf-8 -*-
import scrapy
import re


class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    user_name = "451553616@qq.com"
    user_passwd = "Grt87.=Z[YYC"

    post_data = dict(
        login=user_name,
        password=user_passwd
    )

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata=self.post_data,
            callback=self.after_login
        )



    def after_login(self, response):
        ret = re.findall(r"Qiang", response.body.decode())
        print(ret)
