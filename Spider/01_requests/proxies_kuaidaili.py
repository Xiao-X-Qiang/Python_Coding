import requests
from lxml import etree
import time
from queue import Queue
from threading import Lock
import threading
import random
import json


# 从快代理获取免费代理IP,并进行验证
# 采用多线程，并以Queue进行线程间数据的流动
# 在主程序进行了延时操作(请求响应较慢，此时三队列为空，程序结束)
# 为了避免多次打开文件，在实例化时打开了文件，并对多线程文件写进行了加锁操作，注意，文件必须关闭，内容才可正确写入，故也要作异常处理
# 参考示例：01_requests-->16.spider_qiushibaike_multi_threading
# 在请求时加入随时的时间延时对反爬有显著效果；同时在headers中的User-Agent进行了随机选择；

class SpiderIP(object):
    def __init__(self, page_num):

        self.page_num = page_num

        self.IP_list = []  # 从文件中获取代理IP列表
        with open("./proxies.txt", 'r', encoding="utf8") as f1:
            data = f1.readline()
            while data:
                self.IP_list.append(json.loads(data))
                data = f1.readline()

        user_agents = [  # 用于更换的请求头列表
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        ]

        self.header = {
            "User-Agent": random.choice(user_agents)
        }

        self.lock = Lock()  # 文件锁，用于多线程文件操作时

        self.f = open("./proxies_kuaidaili.txt", "w", encoding="utf8")

        self.url_queue = Queue()
        self.html_queue = Queue()
        self.proxies_queue = Queue()
        self.enable_proxies_queue = Queue()

    def get_proxies(self):
        while True:
            html = self.html_queue.get()
            element = etree.HTML(html)
            tr_list = element.xpath('//tbody/tr')
            for tr in tr_list:
                IP = tr.xpath('./td[1]/text()')[0]
                Port = tr.xpath('./td[2]/text()')[0]
                Cate = tr.xpath('./td[4]/text()')[0]
                proxies = Cate + "://" + IP + ":" + Port
                self.proxies_queue.put(proxies)
                # print(proxies)
            self.html_queue.task_done()

    def verify_proxies(self):
        while True:
            proxies = self.proxies_queue.get()
            proxies = {proxies.split(":", 1)[0]: proxies}
            response = requests.get("http://www.baidu.com", headers=self.header, proxies=proxies)
            if response.status_code == 200:
                self.enable_proxies_queue.put(proxies)
                # print(proxies)
            self.proxies_queue.task_done()

    def save_proxies(self):
        while True:
            proxies = self.enable_proxies_queue.get()

            # with open("./proxies_kuaidaili.txt", "a", encoding="utf8") as f:
            #     f.write(json.dumps(proxies,ensure_ascii=False))
            #     f.write("\n")
            # print(proxies)
            self.lock.acquire()
            self.f.write(json.dumps(proxies, ensure_ascii=False))
            self.f.write("\n")
            self.lock.release()

            self.enable_proxies_queue.task_done()

    def get_html(self):
        while True:
            url = self.url_queue.get()
            proxy = random.choice(self.IP_list)
            time.sleep(random.random())  # 1.加入时间延时
            # response = requests.get(url, headers=self.header)
            # print(proxy)
            response = requests.get(url, headers=self.header, proxies=proxy)  # proxy必须是字符串，从文件读json.loads()
            print(response.url)
            print(response.status_code)
            html = response.content.decode()
            self.html_queue.put(html)
            self.url_queue.task_done()

    def get_url(self):
        for i in range(1, self.page_num):
            self.url_queue.put("https://www.kuaidaili.com/free/inha/{}/".format(i))

    def run(self):

        try:
            t_list = []

            t1 = threading.Thread(target=self.get_url)
            t_list.append(t1)

            t2 = threading.Thread(target=self.get_html)
            t_list.append(t2)

            t3 = threading.Thread(target=self.get_proxies)
            t_list.append(t3)

            t4 = threading.Thread(target=self.verify_proxies)
            t_list.append(t4)

            t5 = threading.Thread(target=self.save_proxies)
            t_list.append(t5)

            for i in t_list:
                i.setDaemon(True)
                i.start()

            # time.sleep(5)  # 加延时，因为请求响应较慢，此时三个队列为空，程序会结束，故而子程序加延时以便请求队列中有内容

            for q in [self.url_queue, self.html_queue, self.proxies_queue, self.enable_proxies_queue]:
                q.join()
        except Exception as result:
            print(result)
        else:
            print("主线程结束")
        finally:
            self.f.close()


def main():
    spiderip = SpiderIP(44)
    spiderip.run()


if __name__ == '__main__':
    main()
