import requests
from lxml import etree
import json
from queue import Queue
import threading
import random
import re


class JieXi_91(object):  # 有bug,有些链接不能解析，待修改

    def random_ip(self):
        a = random.randint(1, 255)
        b = random.randint(1, 255)
        c = random.randint(1, 255)
        d = random.randint(1, 255)
        return (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))

    def __init__(self):

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "referer": "http://91porn.com",
            "X-Forwarded-For": self.random_ip()
        }

        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        with open("91porn.txt", 'r', encoding="utf8") as f:
            while True:
                item = dict()
                data = f.readline()
                if not data:
                    break
                item["title"] = data.strip().split(":", 1)[0]
                item["href"] = data.strip().split(":", 1)[1]
                self.url_queue.put(item)

    def parse_url(self):
        while True:
            url_temp = self.url_queue.get()
            url = url_temp["href"]
            print(url)
            response = requests.get(url, headers=self.headers)
            item = dict()
            item["title"] = url_temp["title"]
            item["content"] = response.content
            self.html_queue.put(item)
            self.url_queue.task_done()

    def get_content_list(self):
        while True:

            html_str_temp = self.html_queue.get()
            html_str = html_str_temp["content"]
            html = etree.HTML(html_str)
            # video_src = html.xpath("//source/@src")[0] if len(html.xpath("//source/@src"))>0 else None

            item = dict()
            item["title"] = html_str_temp["title"]
            item["src"] = re.findall(r'<source src="(.*?)" type=\'video/mp4\'>', str(html_str_temp.content, 'utf-8', errors='ignore'))

            self.content_queue.put(item)
            self.html_queue.task_done()


    def save_content_list(self):
        while True:
            content = self.content_queue.get()

            with open("91porn_src.txt", "a", encoding="utf8") as f:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
            self.content_queue.task_done()


    def run(self):

        t_list = []
        t_url = threading.Thread(target=self.get_url_list)
        t_list.append(t_url)

        for i in range(4):
            t_html = threading.Thread(target=self.parse_url)
            t_list.append(t_html)

        for i in range(3):
            t_content = threading.Thread(target=self.get_content_list)
            t_list.append(t_content)

        for i in range(2):
            t_save = threading.Thread(target=self.save_content_list)
            t_list.append(t_save)

        for i in t_list:
            i.setDaemon(True)
            i.start()

        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()



class Porn_91(object):  # 能获取链接，但名字乱码，待修改

    def random_ip(self):
        a = random.randint(1, 255)
        b = random.randint(1, 255)
        c = random.randint(1, 255)
        d = random.randint(1, 255)
        return (str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))

    def __init__(self):
        self.url_temp = "http://www.91porn.com/v.php?next=watch&page={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "referer": "http://91porn.com",
            "X-Forwarded-For": self.random_ip()
        }

        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        for i in range(3, 8):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url, headers=self.headers)
            self.html_queue.put(response.content)
            self.url_queue.task_done()

    def get_content_list(self):
        while True:
            content_list = []
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            element_list = html.xpath("//div[@class=\"listchannel\"]")
            for i in element_list:
                item = dict()
                item["title"] = i.xpath("./a/@title")[0]

                item["href"] = i.xpath("./a/@href")[0]
                content_list.append(item)
            self.content_queue.put(content_list)
            self.html_queue.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_queue.get()
            with open("91porn.txt", "a", encoding="utf8") as f:
                for i in content_list:
                    f.write(i["title"] + ":")
                    f.write(i["href"] + "\n")
            self.content_queue.task_done()

    def run(self):

        t_list = []
        t_url = threading.Thread(target=self.get_url_list)
        t_list.append(t_url)

        for i in range(4):
            t_html = threading.Thread(target=self.parse_url)
            t_list.append(t_html)

        for i in range(3):
            t_content = threading.Thread(target=self.get_content_list)
            t_list.append(t_content)

        for i in range(2):
            t_save = threading.Thread(target=self.save_content_list)
            t_list.append(t_save)

        for i in t_list:
            i.setDaemon(True)
            i.start()

        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()


def main():
    # 多线程下载91视频链接
    porn_91 = Porn_91()
    porn_91.run()


    # 多线程解析91视频链接
    # jiexi_91 = JieXi_91()
    # jiexi_91.run()


if __name__ == '__main__':
    main()
