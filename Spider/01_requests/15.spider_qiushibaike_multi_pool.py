import requests
from lxml import etree
import json
import multiprocessing


class QiuBai(object):
    def __init__(self):
        self.start_url = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content

    def get_content(self, html_str):
        content = []
        html = etree.HTML(html_str)
        content_list = html.xpath("//*[@id='content']/div/div[2]/div/ul/li[@id]")
        for i in content_list:
            item = {}
            item["title"] = i.xpath(".//a[@class='recmd-content']/text()")
            item["link"] = "https://www.qiushibaike.com" + i.xpath(".//a[@class= 'recmd-content']/@href")[0]
            content.append(item)

        return content

    def save_content(self, content):
        with open("qiubai.txt1", "a", encoding="utf8") as f:
            for i in content:
                f.write(json.dumps(i, ensure_ascii=False))
                f.write("\n")

    def process(self, i):
        url = self.start_url.format(i)
        html_str = self.parse_url(url)

        # 提取数据
        content_list = self.get_content(html_str)
        # 保存数据
        self.save_content(content_list)

    def run(self):

        pool = multiprocessing.Pool(3)
        # 构造url列表
        # 遍历，发送请求，获取响应
        for i in range(1, 14):
            pool.apply_async(self.process, (i,))

        pool.close()
        pool.join()


def main():
    qiubai = QiuBai()
    qiubai.run()


if __name__ == '__main__':
    main()
