# 攫取百度贴吧某一贴下所有的标题及其下的图片
# 关于request.get().xpath中不能正常识别分组，有待于进一步完善
# 注重逻辑的实现，外层循环，内层递归
import requests
from lxml import etree
import json


class TiebaSpider(object):
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "https://tieba.baidu.com/f?kw=" + tieba_name + "=utf-8&pn=0"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def parse_url(self, url):  # 发送请求获得响应
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):

        html = etree.HTML(html_str)
        ul_list = html.xpath("//ul[@id='thread_list']/li")

        content_list = []
        for ul in ul_list:
            item = dict()
            item["href"] = "https://tieba.baidu.com" + ul.xpath(".//a[@class=\"j_th_tit\"]/@href")[0] if len(
                ul.xpath(".//a[@class=\"j_th_tit\"]/@href")) > 0 else None
            item["title"] = ul.xpath(".//a[@class=\"j_th_tit\"]/text()")[0] if len(
                ul.xpath(".//a[@class=\"j_th_tit\"]/text()")) > 0 else None
            item["img_list"] = self.get_img_list(item["href"], [])
            content_list.append(item)
        next_url = "https:" + html.xpath("//a[@class=\"next pagination-item\"]/@href")[0] if len(
            html.xpath("//a[@class=\"next pagination-item\"]/@href")) else None
        return content_list, next_url

    def get_img_list(self, detail_url, total_image_list):  # 内层递归

        # 3.2 请求列表页的url地址，获取详情页的第一页
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)
        # 3.3 提取详情页第一页的图片，提取下一页的地址
        image_list = detail_html.xpath("//img[@class=\"BDE_Image\" and @size]/@src") if len(
            detail_html.xpath("//img[@class=\"BDE_Image\" and @size]/@src")) > 0 else None
        total_image_list.extend(image_list)
        detail_next_url = "https:" + detail_html.xpath("//a[text()=\"下一页\"]/@href")[0]
        # 3.4 请求详情页下一页的地址 ，进行循环3.2-3.4
        if len(detail_next_url) > 0:
            return self.get_img_list(detail_next_url, total_image_list)

        return total_image_list

    def save_content_list(self, content_list):
        file_path = self.tieba_name + ".txt"
        with open(file_path, 'a', encoding="utf8") as f:
            f.write(json.dumps(content_list, ensure_ascii=False, indent=2))
            f.write("\n")
        print("保存成功")

    def run(self):  # 实现主要的逻辑
        next_url = self.start_url
        while next_url is not None:  # 外层循环
            # 1.start_url
            # 2.请求获取响应
            html_str = self.parse_url(next_url)
            # 3.提取数据，及下一页的url
            # 3.1 提取列表页的url地址和标题
            # 3.2 请求列表页的url地址，获取详情页的第一页
            # 3.3 提取详情页第一页的图片，提取下一页的地址
            # 3.4 请求详情页下一页的地址 ，进行循环3.2-3.4
            content_list, next_url = self.get_content_list(html_str)
            # 4.保存数据
            self.save_content_list(content_list)

            # 5.请求下一页，进行循环2.5


def main():
    tieba_spider = TiebaSpider("美女吧")
    tieba_spider.run()


if __name__ == '__main__':
    main()
