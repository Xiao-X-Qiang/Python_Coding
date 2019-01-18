
# -*- coding: utf-8 -*-
import scrapy
import re


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        user_name = "451553616@qq.com"
        user_passwd = "Grt87.=Z[YYC"

        login_url = "https://github.com/session"
        post_data = dict(
            commit=commit,
            utf8=utf8,
            authenticity_token=authenticity_token,
            login=user_name,
            password=user_passwd
        )

        yield scrapy.FormRequest(
            login_url,
            callback=self.after_login,
            formdata=post_data
        )

    def after_login(self, response):
        ret = re.findall(r"Qiang", response.body.decode())
        print(ret)
