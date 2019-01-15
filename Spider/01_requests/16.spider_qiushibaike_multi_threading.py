import requests
from lxml import etree
import json
import threading
from queue import Queue


class QiuBai(object):
    def __init__(self):
        self.start_url = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            print(url)
            response = requests.get(url, headers=self.headers)
            # return response.content
            self.html_queue.put(response.content)
            self.url_queue.task_done()

    def get_content(self):
        while True:
            content = []
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            content_list = html.xpath("//*[@id='content']/div/div[2]/div/ul/li[@id]")
            for i in content_list:
                item = {}
                item["title"] = i.xpath(".//a[@class='recmd-content']/text()")
                item["link"] = "https://www.qiushibaike.com" + i.xpath(".//a[@class= 'recmd-content']/@href")[0]
                content.append(item)

            self.content_queue.put(content)
            self.html_queue.task_done()

    def save_content(self):
        while True:
            content = self.content_queue.get()
            with open("qiubai.txt", "a", encoding="utf8") as f:
                for i in content:
                    f.write(json.dumps(i, ensure_ascii=False))
                    f.write("\n")
            self.content_queue.task_done()  # content_queue队列计数减一，否则的话，queue.join()永远会阻塞

    def get_url_list(self):
        for i in range(1, 14):
            self.url_queue.put(self.start_url.format(i))

    def run(self):
        # 构造url列表
        # 遍历，发送请求，获取响应
        queue_list = []

        t_url = threading.Thread(target=self.get_url_list)
        queue_list.append(t_url)

        for i in range(3):
            t_html = threading.Thread(target=self.parse_url)
            queue_list.append(t_html)

        t_content = threading.Thread(target=self.get_content)
        queue_list.append(t_content)

        t_save = threading.Thread(target=self.save_content)
        queue_list.append(t_save)

        print(queue_list)
        for i in queue_list:
            i.setDaemon(True)  # 设为守护线程，如果主线程结束，子线程也结束
            i.start()

        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()  # 所有的队列长度为0时，方解阻塞
        print("主线程结束")


def main():
    qiubai = QiuBai()
    qiubai.run()


if __name__ == '__main__':
    main()
